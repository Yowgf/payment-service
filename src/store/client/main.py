import sys

from common import log
from .client import StoreClient
from .config import parse_config

logger = log.logger('payment-service-store-client')

def main():
    try:
        log.parse_config_log_level(sys.argv[1:])

        logger.info("Starting store client.")

        logger.info(f"Program got arguments: {sys.argv[1:]}")

        config = parse_config(sys.argv[1:])
        client = StoreClient(config)
        client.init()
        client.run()

        logger.info("Successfully ran store client. Terminating gracefully.")

    except Exception as e:
        logger.critical(f"Encountered fatal error: {e}", exc_info=True)
