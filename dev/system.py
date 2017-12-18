from sqlalchemy.orm import sessionmaker
from db import *
from datetime import datetime, date
from manager import UserManager, SubscriptionManager

Session = sessionmaker(bind = engine)

class System(object):
    def __init__(self):
        Base.metadata.create_all(engine)
        self.user_manager = UserManager(Session)
        self.subscription_manager = SubscriptionManager(Session)
