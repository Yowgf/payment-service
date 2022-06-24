import sys

from common import log
from .client import Client
from .config import parse_config

logger = log.logger('payment-service-bank-client')

def main():
    try:
        logger.info("Starting bank client.")

        logger.info(f"Program got arguments: {sys.argv[:1]}")

        config = parse_config(sys.argv[1:])
        client = Client(config)
        client.init()
        client.run()

        logger.info("Successfully ran bank client. Terminating gracefully.")

    except Exception as e:
        logger.critical(f"Encountered fatal error: {e}", exc_info=True)
