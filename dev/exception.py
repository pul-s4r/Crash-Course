class Error(Exception):
    """Base class for exceptions in this module"""
    pass

class EmptyFieldError(Error):
    """Raised when nothing is passed into required text fields"""
    pass

class SpaceError(Error):
    """Raised when space is not allowed in input"""
    pass
