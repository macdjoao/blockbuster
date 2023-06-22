from datetime import date


def param_is_none(arg):
    if arg == None:
        return True
    return False


def param_is_not_a_string(*args):
    for arg in args:
        if not isinstance(arg, str):
            return True
    return False


def param_is_not_a_date(*args):
    for arg in args:
        if not isinstance(arg, date):
            return True
    return False


def param_is_not_a_bool(*args):
    for arg in args:
        if not isinstance(arg, bool):
            return True
    return False


def param_is_not_a_recognized_attribute(object, arg):
    if not (hasattr(object, f'{arg}')):
        return True
    return False


def id_not_found(session, object, arg):
    data_update = session.query(object).filter(object.id == arg).first()
    if data_update is None:
        return True
    return False


def email_already_registered(session, object, email):
    data = session.query(object).filter(object.email == email).first()
    if data is None:
        return True
    return False


def param_is_not_a_int(*args):
    for arg in args:
        if not isinstance(arg, int):
            return True
    return False
