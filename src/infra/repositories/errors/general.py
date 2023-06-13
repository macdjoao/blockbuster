class IncompleteParams(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.message = 'Error: Incomplete params'


class ParamIsNotString(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.message = 'Error: Param is not a string'


class ParamIsNotDate(Exception):
    def __init__(self) -> None:
        super().__init__()
        self.message = 'Error: Param is not a date'
