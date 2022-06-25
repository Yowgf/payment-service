import bank_pb2

from common import log
from .defs import LOGGER_NAME
from .wallet import Wallet

logger = log.logger(LOGGER_NAME)

class BankService:
    def __init__(self, wallets_file):
        wfile_lines = open(wallets_file).read().strip().split("\n")
        wfile_entries = [line.split(" ") for line in wfile_lines]
        logger.debug("Wallet file entries: {}".format(wfile_entries))
        self._wallets = [Wallet(entry[0], int(entry[1])) for entry in wfile_entries]

    def GetBalance(self, request, context):
        walletid = request.walletId
        logger.debug("Received GetBalance request. walletId: {}".format(
            walletid))

        balance = -1
        req_wallet = None
        for wallet in self._wallets:
            if wallet.id == walletid:
                req_wallet = wallet
                break
        if req_wallet != None:
            balance = req_wallet.balance

        resp = bank_pb2.GetBalanceResponse(balance=balance)

        logger.debug("Successfully processed GetBalance request. balance: {}".format(
            balance))

        return resp

    def Pay(self, request, context):
        return bank_pb2.PayResponse(orderId="", status=0)

    def Transfer(self, request, context):
        return bank_pb2.TransferResponse(status=0)

    def KillServer(self, request, context):
        return bank_pb2.KillServerResponse(numAccounts=0)
