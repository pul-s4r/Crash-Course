from system import *
from abc import ABCMeta
from werkzeug.security import generate_password_hash
from datetime import datetime

db_command = DBCommand()

class Manager(metaclass = ABCMeta):
    """Abstract manager class"""
    def __init__(self, db_session):
        super(Manager, self).__init__()
        self._db_session = db_session

class UserManager(Manager):
    """Handles User class"""
    def __init__(self, db_session):
        # Calls superconstructor (Manager class constructor)
        super(UserManager, self).__init__(db_session)

    def add_user(self, username, password, fname, lname, email, dob):
        session = self._db_session()
        hash_pw = generate_password_hash(password)
        dob = datetime.strptime(dob, "%d/%m/%Y").date()
        user = User(id = None,
                    username = username,
                    hash_pw = hash_pw,
                    fname = fname,
                    lname = lname,
                    email = email,
                    dob = dob)
        db_command.add_row(session, user)
        return user
