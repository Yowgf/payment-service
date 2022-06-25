class Config:
    def __init__(self, product_price, port, walletid, bank_endpoint):
        self.product_price = product_price
        self.port = port
        self.walletid = walletid
        self.bank_endpoint = bank_endpoint

def parse_config(args):
    min_args = 4
    if len(args) < min_args:
        raise ValueError(f"Need at least {min_args} arguments for the program")

    product_price = int(args[0])
    port = int(args[1])
    walletid = args[2]
    bank_endpoint = args[3]

    return Config(product_price, port, walletid, bank_endpoint)
