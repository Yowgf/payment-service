import concurrent.futures
import time

import grpc

import bank_pb2
import bank_pb2_grpc
from common import log
from .defs import LOGGER_NAME

logger = log.logger(LOGGER_NAME)

class BankServer:
    def __init__(self, config):
        self._port = config.port
        self._wallets_file = config.wallets_file

        self._stop = False

    def init(self):
        logger.info("Initializing Bank server")

        self._srv = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
        self._srv.GetBalance = self._GetBalance
        self._srv.Pay = self._Pay
        self._srv.Transfer = self._Transfer
        self._srv.KillServer = self._KillServer

        # Register grpc service
        bank_pb2_grpc.add_BankServicer_to_server(bank_pb2_grpc.BankServicer(),
                                                self._srv)
        self._srv.add_insecure_port("[::]:{}".format(self._port))

        logger.info("Successfully initialized Bank server")

    def run(self):
        logger.info("Starting Bank server.")

        self._srv.start()
        while not self._stop:
            time.sleep(5)

        logger.info("Terminating Bank server.")

    def _GetBalance(self, request, context):
        print("Got wallet id: {}".format(request.walletId))

    def _Pay(self, request, context):
        pass

    def _Transfer(self, request, context):
        pass

    def _KillServer(self, request, context):
        pass
