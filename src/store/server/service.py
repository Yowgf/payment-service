import secrets

import store_pb2

from common import log
from .defs import LOGGER_NAME

logger = log.logger(LOGGER_NAME)

class StoreService:
    def __init__(self):
        pass

    def GetProductPrice(self, request, context):
        logger.debug("Received GetProductPrice request: {}".format(request))

        resp = store_pb2.GetProductPriceResponse(price=0)

        logger.debug("Successful GetProductPrice request. resp: {}".format(resp))

        return resp

    def SellProduct(self, request, context):
        logger.debug("Received SellProduct request: {}".format(request))

        resp = SellProductResponse(price=0)

        logger.debug("Successful SellProduct request. resp: {}".format(resp))

        return resp

    def KillServer(self, request, context):
        # TODO: return right number of accounts
        return store_pb2.KillServerResponse(storeBalance=0)
