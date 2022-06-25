import sys

import grpc

from common import log
from .config import Config
from .defs import LOGGER_NAME
from .request import Request

import bank_pb2
import bank_pb2_grpc

logger = log.logger(LOGGER_NAME)

class BankClient:
    def __init__(self, config):
        self._walletid = config.walletid
        self._server_location = config.server_location
        logger.info(f"Received config: walletid={self._walletid} "+
                    f"server_location={self._server_location}")

        self._orders = {}
        # This order alias is used locally by the client to keep track of
        # payment orders it sent to the server.
        self._order_alias = 1

    def init(self):
        pass

    def run(self):
        instr = ""
        channel = grpc.insecure_channel(self._server_location)
        stub = bank_pb2_grpc.BankStub(channel)
        while True:
            request_str = input()
            request = self._parse_request(request_str)
            self._process_request(stub, self._walletid, request)
            if request.type == Request.KILL_SERVER:
                break

    def _parse_request(self, request_str):
        split_by_space = request_str.strip().split(" ")
        request_type = split_by_space[0]
        args = []

        # S
        if request_type == Request.GET_BALANCE:
            assert len(split_by_space) == 1
        # O <payment_value>
        elif request_type == Request.PAY:
            assert len(split_by_space) == 2
            payment_value = int(split_by_space[1])
            args.append(payment_value)
        # X <transfer_value> <token> <target_walletid>
        elif request_type == Request.TRANSFER:
            assert len(split_by_space) == 4
            transfer_value = int(split_by_space[1])
            order_token = split_by_space[2].encode('ascii')
            assert len(order_token) == 1
            walletid = split_by_space[3]
            args.extend([transfer_value, order_token, walletid])
        # F
        elif request_type == Request.KILL_SERVER:
            assert len(split_by_space) == 1
        else:
            raise ValueError(f"Invalid request type '{request_str}'")

        return Request(request_type, args)

    def _process_request(self, stub, walletid, request):
        if request.type == Request.GET_BALANCE:
            req = bank_pb2.GetBalanceRequest(walletId=walletid)
            resp = stub.GetBalance(req)
            print(resp.balance)
        elif request.type == Request.PAY:
            req = bank_pb2.PayRequest(walletId=walletid, amount=request.args[0])
            resp = stub.Pay(req)
            status = resp.status
            if status < 0:
                print("{}".format(resp.status))
            else:
                self._orders[self._order_alias] = resp.orderId
                print("{}".format(self._order_alias))
                self._order_alias += 1
        elif request.type == Request.TRANSFER:
            order_alias = int(request.args[1])
            logger.debug("Order alias for transfer request: {}".format(order_alias))
            if order_alias not in self._orders:
                status = -9
                print("{}".format(status))
            else:
                orderid = self._orders[order_alias]
                req = bank_pb2.TransferRequest(amount=request.args[0],
                                               orderId=orderid,
                                               targetWalletId=request.args[2])
                resp = stub.Transfer(req)
                print("{}".format(resp.status))
        elif request.type == Request.KILL_SERVER:
            req = bank_pb2.KillServerRequest()
            resp = stub.KillServer(req)
            print("{}".format(resp.numAccounts))
        else:       
            raise ValueError(f"Invalid request type '{request_str}'")
