from common import log

class Config:
    def __init__(self, walletid, server_location):
        self.walletid = walletid
        self.server_location = server_location

def parse_config(args):
    min_args = 2
    if len(args) < min_args:
        raise ValueError(f"Need at least {min_args} arguments for the program")

    walletid = args[0]
    server_location = args[1]

    return Config(walletid, server_location)
