import sys

import grpc

from common import log
from .config import Config
from .defs import LOGGER_NAME

import bank_pb2
import bank_pb2_grpc

logger = log.logger(LOGGER_NAME)

class Command:
    GET_BALANCE = "S"
    PAY         = "O"
    TRANSFER    = "X"
    KILL_SERVER = "F"

    def __init__(self, type, args):
        self.type = type
        self._args = args

    def execute(self, walletid, stub):
        if self.type == Command.GET_BALANCE:
            req = bank_pb2.GetBalanceRequest(walletId=walletid)
            resp = stub.GetBalance(req)
            logger.info("GetBalance response: {}".format(resp))
        elif self.type == Command.PAY:
            pass
        elif self.type == Command.TRANSFER:
            pass
        elif self.type == Command.KILL_SERVER:
            pass
        else:
            raise ValueError(f"Invalid command {s}")        

    def parse(s):
        split_by_space = s.strip().split(" ")
        command_type = split_by_space[0]
        args = []

        # S
        if command_type == Command.GET_BALANCE:
            assert len(split_by_space) == 1
        # O <payment_value>
        elif command_type == Command.PAY:
            assert len(split_by_space) == 2
            payment_value = int(split_by_space[1])
            args.append(payment_value)
        # X <transfer_value> <token> <walletid>
        elif command_type == Command.TRANSFER:
            assert len(split_by_space) == 4
            transfer_value = int(split_by_space[1])
            order_token = split_by_space[2].encode('ascii')
            assert len(order_token) == 1
            walletid = split_by_space[3]
            args.extend([transfer_value, order_token, walletid])
        # F
        elif command_type == Command.KILL_SERVER:
            assert len(split_by_space) == 1
        else:
            raise ValueError(f"Invalid command {s}")

        return Command(command_type, args)

class BankClient:

    def __init__(self, config):
        self._wallet_id = config.wallet_id
        self._server_location = config.server_location
        logger.info(f"Received config: wallet_id={self._wallet_id} "+
                    f"server_location={self._server_location}")

    def init(self):
        pass

    def run(self):
        instr = ""
        channel = grpc.insecure_channel(self._server_location)
        stub = bank_pb2_grpc.BankStub(channel)
        while True:
            instr = input()
            command = Command.parse(instr)
            command.execute(self._wallet_id, stub)
            if command.type == Command.KILL_SERVER:
                break
