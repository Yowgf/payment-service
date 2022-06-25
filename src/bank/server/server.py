import concurrent.futures
import time

import grpc

import bank_pb2
import bank_pb2_grpc
from common import log
from .defs import LOGGER_NAME
from .service import BankService

logger = log.logger(LOGGER_NAME)

class BankServer:
    def __init__(self, config):
        self._port = config.port
        self._wallets_file = config.wallets_file

        self._stop = False

    def init(self):
        logger.info("Initializing Bank server")

        # Register grpc service
        service = BankService(self._wallets_file)
        self._srv = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
        bank_pb2_grpc.add_BankServicer_to_server(service,
                                                self._srv)
        self._srv.add_insecure_port("[::]:{}".format(self._port))

        logger.info("Successfully initialized Bank server")

    def run(self):
        logger.info("Starting Bank server.")

        self._srv.start()
        while not self._stop:
            time.sleep(5)

        logger.info("Terminating Bank server.")
