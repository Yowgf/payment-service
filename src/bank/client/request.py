class Request:
    GET_BALANCE = "S"
    PAY         = "O"
    TRANSFER    = "X"
    KILL_SERVER = "F"

    def __init__(self, type, args):
        self.type = type
        self.args = args
