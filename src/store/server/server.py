import concurrent.futures
import time

import grpc

import store_pb2
import store_pb2_grpc
from common import log
from .defs import LOGGER_NAME
from .service import StoreService

logger = log.logger(LOGGER_NAME)

class StoreServer:
    def __init__(self, config):
        self._product_price = config.product_price
        self._port = config.port
        self._walletid = config.walletid
        self._bank_endpoint = config.bank_endpoint

        self._stop = False

    def init(self):
        logger.info("Initializing Store server")

        # Register grpc service
        service = StoreService(self._product_price, self._walletid,
                               self._bank_endpoint)
        self._srv = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=4))
        store_pb2_grpc.add_StoreServicer_to_server(service,
                                                self._srv)
        self._srv.add_insecure_port("[::]:{}".format(self._port))

        logger.info("Successfully initialized Store server")

    def run(self):
        logger.info("Starting Store server.")

        self._srv.start()
        while not self._stop:
            time.sleep(5)

        logger.info("Terminating Store server.")
