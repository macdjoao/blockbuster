class IncompleteParamError(Exception):
    def __init__(self, arg) -> None:
        super().__init__()
        self.arg = arg
        self.message = f'Error: Incomplete param "{self.arg}"'


class ParamIsNotStringError(Exception):
    def __init__(self, arg) -> None:
        super().__init__()
        self.arg = arg
        self.message = f'Error: Param "{self.arg}" must be a string'


class ParamIsNotDateError(Exception):
    def __init__(self, error_param) -> None:
        super().__init__()
        self.error_param = error_param
        self.message = f'Error: Param {error_param} must be a date'


class ParamIsNotBoolError(Exception):
    def __init__(self, error_param) -> None:
        super().__init__()
        self.error_param = error_param
        self.message = f'Error: Param {error_param} must be a boolean'


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


class EmailAlreadyRegisteredError(Exception):
    def __init__(self, email: str) -> None:
        super().__init__()
        self.email = email
        self.message = f'Error: Email "{self.email} is already registered"'


class ParamIsNotIntegerError(Exception):
    def __init__(self, arg) -> None:
        super().__init__()
        self.arg = arg
        self.message = f'Error: Param "{self.arg}" must be a integer'
