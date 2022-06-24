from common import log

class Config:
    def __init__(self, wallet_id, server_location):
        self.wallet_id = wallet_id
        self.server_location = server_location

def parse_config(args):
    log.parse_config_log_level(args)

    min_args = 2
    if len(args) < min_args:
        raise ValueError("Need at least {min_args} arguments for the program")

    wallet_id = args[0]
    server_location = args[1]

    return Config(wallet_id, server_location)
