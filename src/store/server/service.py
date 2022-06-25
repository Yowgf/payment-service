import grpc

import bank_pb2
import bank_pb2_grpc
import store_pb2
from common import log
from .defs import LOGGER_NAME

logger = log.logger(LOGGER_NAME)

class StoreService:
    def __init__(self, product_price, walletid, bank_endpoint, stop_event):
        self._product_price = product_price
        self._walletid = walletid
        self._bank_endpoint = bank_endpoint
        self._stop_event = stop_event

        bank_channel = grpc.insecure_channel(bank_endpoint)
        self._bank_stub = bank_pb2_grpc.BankStub(bank_channel)

        self._store_balance = 0

    def GetProductPrice(self, request, context):
        logger.debug("Received GetProductPrice request: {}".format(request))

        resp = store_pb2.GetProductPriceResponse(price=self._product_price)

        logger.debug("Successful GetProductPrice request. resp: {}".format(resp))

        return resp

    def SellProduct(self, request, context):
        logger.debug("Received SellProduct request: {}".format(request))

        orderid = request.orderId

        transfer_req = bank_pb2.TransferRequest(targetWalletId=self._walletid,
                                                orderId=orderid,
                                                amount=self._product_price)
        transfer_resp = self._bank_stub.Transfer(transfer_req)

        transfer_status = transfer_resp.status

        if transfer_status < 0:
            status = -9
        else:
            status = transfer_status
            self._store_balance = status

        resp = store_pb2.SellProductResponse(price=status)

        logger.debug("Successful SellProduct request. resp: {}".format(resp))

        return resp

    def KillServer(self, request, context):
        logger.debug("Received KillServer request: {}".format(request))

        self._stop_event.set()
        resp = store_pb2.KillServerResponse(storeBalance=self._store_balance)

        logger.debug("Successful KillServer request. resp: {}".format(resp))

        return resp
