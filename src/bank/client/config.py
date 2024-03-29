from common import log

class Config:
    def __init__(self, walletid, bank_endpoint):
        self.walletid = walletid
        self.bank_endpoint = bank_endpoint

def parse_config(args):
    min_args = 2
    if len(args) < min_args:
        raise ValueError(f"Need at least {min_args} arguments for the program")

    walletid = args[0]
    bank_endpoint = args[1]

    return Config(walletid, bank_endpoint)
