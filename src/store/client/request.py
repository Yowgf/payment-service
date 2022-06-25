class Request:
    GET_PRODUCT_PRICE = "P"
    SELL_PRODUCT      = "C"
    KILL_SERVER       = "T"

    def __init__(self, type, args):
        self.type = type
        self.args = args
