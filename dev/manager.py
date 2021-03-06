from abc import ABCMeta
from werkzeug.security import generate_password_hash
from datetime import datetime
from db import *
from input_validation import check_empty_field, check_spacebar

class Manager(metaclass = ABCMeta):
    """Abstract manager class that contains functionality when interacting
    with the database
    """
    def __init__(self, db_session):
        super().__init__()
        self._db_session = db_session

    """Adds row, commits and closes session"""
    def _add_row(self, session, row):
        session.add(row)
        session.commit()
        session.close()

    """Deletes row, commits and closes session"""
    def _delete_row(self, session, row):
        session.delete(row)
        session.commit()
        session.close()

class UserManager(Manager):
    """Handles User class"""
    def __init__(self, db_session):
        # Calls superconstructor (Manager class constructor)
        super().__init__(db_session)

    def add_user(self, username, password, fname, lname, email, dob, gender):
        # Checks for empty field
        check_empty_field(username)
        check_empty_field(password)
        check_empty_field(fname)
        check_empty_field(lname)
        check_empty_field(email)
        check_empty_field(dob)
        check_empty_field(gender)

        # Checks for space in input
        check_spacebar(username)
        check_spacebar(email)

        # Create a session
        session = self._db_session()
        # Hashes password using PBKDF2
        hash_pw = generate_password_hash(password)
        # Converts date format of dd/mm/YYYY to a date object
        dob = datetime.strptime(dob, "%d/%m/%Y").date()
        user = User(id = None,
                    username = username,
                    hash_pw = hash_pw,
                    fname = fname,
                    lname = lname,
                    email = email,
                    dob = dob,
                    gender = gender)
        self._add_row(session, user)

    def query_user(self, username):
        session = self._db_session()
        user = session.query(User).filter(User.username == username).one()
        session.close()
        return user

class SubscriptionManager(Manager):
    """Handles User class"""
    def __init__(self, db_session):
        # Calls superconstructor (Manager class constructor)
        super().__init__(db_session)

    def subscribe(self, user_id, channel_id, subscribe_date):
        session = self._db_session()
        subscription = Subscription(subscriber_id = user_id,
                                    channel_id = channel_id,
                                    subscribe_date = subscribe_date)
        self._add_row(session, subscription)
