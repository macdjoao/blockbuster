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


class ParamAreNotRecognizedError(Exception):
    def __init__(self, error_param) -> None:
        super().__init__()
        self.error_param = error_param
        self.message = f'Error: Param "{self.error_param}" is not recognized as a attribute'


class IdNotFoundError(Exception):
    def __init__(self, id) -> None:
        super().__init__()
        self.id = id
        self.message = f'Error: Id "{self.id}" not found'
