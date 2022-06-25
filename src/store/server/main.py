import sys

from common import log
from .server import StoreServer
from .config import parse_config

logger = log.logger('payment-service-store-server')

def main():
    try:
        log.parse_config_log_level(sys.argv[1:])

        logger.info("Starting store server.")

        logger.info(f"Program got arguments: {sys.argv[1:]}")

        config = parse_config(sys.argv[1:])
        server = StoreServer(config)
        server.init()
        server.run()

        logger.info("Successfully ran store server. Terminating gracefully.")

    except Exception as e:
        logger.critical(f"Encountered fatal error: {e}", exc_info=True)
