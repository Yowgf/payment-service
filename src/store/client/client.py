import sys

import grpc

import bank_pb2
import bank_pb2_grpc
import store_pb2
import store_pb2_grpc
from common import log
from .defs import LOGGER_NAME
from .request import Request

logger = log.logger(LOGGER_NAME)

class StoreClient:
    def __init__(self, config):
        self._walletid = config.walletid
        self._bank_endpoint = config.bank_endpoint
        self._store_endpoint = config.store_endpoint

    def init(self):
        bank_channel = grpc.insecure_channel(self._bank_endpoint)
        self._bank_stub = bank_pb2_grpc.BankStub(bank_channel)
        store_channel = grpc.insecure_channel(self._store_endpoint)
        self._store_stub = store_pb2_grpc.StoreStub(store_channel)

    def run(self):
        instr = ""
        while True:
            request_str = input()
            request = self._parse_request(request_str)
            self._process_request(self._walletid, request)
            if request.type == Request.KILL_SERVER:
                break

    def _parse_request(self, request_str):
        split_by_space = request_str.strip().split(" ")
        request_type = split_by_space[0]
        args = []

        # P
        if request_type == Request.GET_PRODUCT_PRICE:
            assert len(split_by_space) == 1
        # C
        elif request_type == Request.SELL_PRODUCT:
            assert len(split_by_space) == 1
        # T
        elif request_type == Request.KILL_SERVER:
            assert len(split_by_space) == 1
        else:
            raise ValueError(f"Invalid request type '{request_str}'")

        return Request(request_type, args)

    def _process_request(self, walletid, request):
        if request.type == Request.GET_PRODUCT_PRICE:
            req = store_pb2.GetProductPriceRequest()
            resp = self._store_stub.GetProductPrice(req)
            product_price = resp.price

            req = bank_pb2.GetBalanceRequest(walletId=self._walletid)
            resp = self._bank_stub.GetBalance(req)
            wallet_balance = resp.balance

            print("{} {}".format(product_price, wallet_balance))
        elif request.type == Request.SELL_PRODUCT:
            pass
        elif request.type == Request.KILL_SERVER:
            req = store_pb2.KillServerRequest()
            resp = self._store_stub.KillServer(req)
            print("{}".format(resp.storeBalance))
        else:       
            raise ValueError(f"Invalid request type '{request_str}'")
