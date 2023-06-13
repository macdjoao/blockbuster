class IncompleteParamsError(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.message = 'Error: Incomplete params'


class ParamIsNotStringError(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.message = 'Error: Param is not a string'


class ParamIsNotDateError(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.message = 'Error: Param is not a date'
