class Config:
    def __init__(self, port, wallets_file):
        self.port = port
        self.wallets_file = wallets_file

def parse_config(args):
    min_args = 2
    if len(args) < min_args:
        raise ValueError(f"Need at least {min_args} arguments for the program")

    port = args[0]
    wallets_file = args[1]

    return Config(port, wallets_file)
