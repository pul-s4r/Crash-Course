from sqlalchemy import Table, Column, Integer, String, Date, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from flask_login import UserMixin

db_string = "sqlite:///crash_course.db" # Database name

engine = create_engine(db_string) # Abstraction of database and its API

# Creates a base class that creates appropriate
# tables from classes that inherit from it
Base = declarative_base()
Base.metadata.bind = engine

class Subscription(Base):
    """Table that contains many to many
    relationship between a user and a channel

    """
    __tablename__ = "subscription"

    subscriber_id = Column(Integer, ForeignKey("user.id"), primary_key = True)
    channel_id = Column(Integer, ForeignKey("user.id"), primary_key = True)
    subscribe_date = Column(Date)

class User(Base, UserMixin):
    """Table that contains user information"""
    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    username = Column(String, nullable = False, unique = True)
    hash_pw = Column(String, nullable = False)
    fname = Column(String, nullable = False)
    lname = Column(String, nullable = False)
    email = Column(String(320), nullable = False, unique = True)
    dob = Column(Date, nullable = False)
    gender = Column(String, nullable = False)
    subscribers = relationship("Subscription",
                               backref = "subcriber",
                               primaryjoin = id == Subscription.subscriber_id)
    channels = relationship("Subscription",
                            backref = "channel",
                            primaryjoin = id == Subscription.channel_id)

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def get_hash_pw(self):
        return self.hash_pw

    def get_fname(self):
        return self.fname

    def get_lname(self):
        return self.lname

    def get_email(self):
        return self.email

    def get_dob(self):
        return self.dob.strftime("%d/%m/%Y")

    def get_gender(self):
        return self.gender

"""class Category(Base):
    Table that contains types of streaming categories
    __tablename__ = "category"

    id = Column(Integer, primary_key = True)
    category = Column(String, nullable = False)

class Interest(Base):
    Table that contains many to many
    relationship between user and category
    __tablename__ = "interest"

    id = Column(Integer, primary_key = True)
    user = relationship("user", lazy = "joined")
    category = relationship("category", lazy = "joined")"""
