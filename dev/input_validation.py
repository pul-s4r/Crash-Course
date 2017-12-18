from exception import EmptyFieldError, SpaceError

def check_empty_field(val):
    if not val:
        raise EmptyFieldError

def check_spacebar(val):
    if " " in val:
        raise SpaceError
