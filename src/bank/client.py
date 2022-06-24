import sys

from common import log
from .config import Config

logger = log.logger('payment-service-bank-client')

class Client:
    def __init__(self, config):
        self._wallet_id = config.wallet_id
        self._server_location = config.server_location
        logger.info(f"Received config: wallet_id={self._wallet_id} "+
                    f"server_location={self._server_location}")

    def init(self):
        pass

    def run(self):
        pass

def parse_config(args):
    log.parse_config_log_level(args)

    min_args = 2
    if len(args) < min_args:
        raise ValueError("Need at least {min_args} arguments for the program")

    wallet_id = args[0]
    server_location = args[1]

    return Config(wallet_id, server_location)
