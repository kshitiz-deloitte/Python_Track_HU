class FormulaError(Exception):
    def __init__(self, *args: object):
        super().__init__(args)
        self.message = args[0]
    pass