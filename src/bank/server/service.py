import secrets

import bank_pb2

from common import log
from .defs import LOGGER_NAME
from .wallet import Wallet
from .order import Order

logger = log.logger(LOGGER_NAME)

class BankService:
    _orderid_size = 32

    def __init__(self, wallets_file):
        wfile_lines = open(wallets_file).read().strip().split("\n")
        wfile_entries = [line.split(" ") for line in wfile_lines]
        logger.debug("Wallet file entries: {}".format(wfile_entries))

        self._wallets = {}
        for entry in wfile_entries:
            walletid = entry[0]
            balance = int(entry[1])
            self._wallets[walletid] = Wallet(walletid, balance)

        self._orders = {}

    def GetBalance(self, request, context):
        walletid = request.walletId
        logger.debug("Received GetBalance request: {}".format(request))

        balance = -1
        req_wallet = self._find_wallet(walletid)
        if req_wallet != None:
            balance = req_wallet.balance

        resp = bank_pb2.GetBalanceResponse(balance=balance)

        logger.debug("Successful GetBalance request. resp: {}".format(resp))

        return resp

    def Pay(self, request, context):
        logger.debug("Received Pay request: {}".format(request))

        walletid = request.walletId
        amount = request.amount

        status = 0
        wallet = self._find_wallet(walletid)
        if wallet == None:
            status = -1
        elif amount > wallet.balance:
            status = -2

        if status < 0:
            orderid = ('-'*self._orderid_size).encode()
        else:
            orderid = secrets.token_bytes(self._orderid_size)
            self._orders[orderid] = Order(orderid, wallet, amount)

        resp = bank_pb2.PayResponse(orderId=orderid, status=status)

        logger.debug("Successful Pay request. resp: {}".format(resp))

        return resp

    def Transfer(self, request, context):
        target_walletid = request.targetWalletId
        orderid = request.orderId
        amount = request.amount
        logger.debug("Received Transfer request: {}".format(request))

        status = 0
        target_wallet = self._find_wallet(target_walletid)
        if target_wallet == None:
            status = -1
        elif orderid not in self._orders:
            status = -2
        elif amount != self._orders[orderid].amount:
            status = -3

        if status >= 0:
            order = self._orders.pop(orderid)
            walletid = target_walletid
            self._wallets[walletid].balance += order.amount
            status = self._wallets[walletid].balance

        resp = bank_pb2.TransferResponse(status=status)

        logger.debug("Successful Transfer request. resp: {}".format(resp))

        return resp

    def KillServer(self, request, context):
        # TODO: return right number of accounts
        return bank_pb2.KillServerResponse(numAccounts=0)

    def _find_wallet(self, walletid):
        if walletid in self._wallets:
            return self._wallets[walletid]
        return None
