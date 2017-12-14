from sqlalchemy.orm import sessionmaker
from db import *
from datetime import datetime
from manager import UserManager

Session = sessionmaker(bind = engine)

class System(object):
    def __init__(self):
        Base.metadata.create_all(engine)
        self.user_manager = UserManager(Session)
