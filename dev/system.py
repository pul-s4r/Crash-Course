from sqlalchemy.orm import sessionmaker
from db import *
from datetime import datetime
from manager import UserManager

Session = sessionmaker(bind = engine)

class System(object):
    def __init__(self):
        Base.metadata.create_all(engine)
        self.user_manager = UserManager(Session)

class DBCommand(object):
    """Handles generic database commands"""
    def add_row(session, row):
        session.add(row)
        session.commit()
        session.close()

    def delete_row(session, row):
        session.delete(row)
        session.commit()
        session.close()

system = System()
user = system.user_manager.add_user("Khu",
                                    "password",
                                    "Kent",
                                    "Hu",
                                    "khu.1998@icloud.com",
                                    "17/06/1998")
