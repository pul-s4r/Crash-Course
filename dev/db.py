from sqlalchemy import Table, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from flask_login import UserMixin

db_string = "sqlite:///crash_course.db" # Database name
engine = create_engine(db_string)

Base = declarative_base()

class User(Base, UserMixin):
    """Table that contains user information"""
    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    username = Column(String, nullable = False, unique = True)
    fname = Column(String, nullable = False)
    lname = Column(String, nullable = False)
    password = Column(String, nullable = False)

class Subscription(Base):
    """Table that contains many to many
    relationship between a user and a channel"""
    __tablename__ = "subscription"

    id = Column(Integer, primary_key = True)
    subcriber = relationship("user", lazy = "joined")
    channel = relationship("user", lazy = "joined")

class Category(Base):
    """Table that contains types of streaming categories"""
    __tablename__ = "category"

    id = Column(Integer, primary_key = True)
    category = Column(String, nullable = False)

class Interest(Base):
    """Table that contains many to many
    relationship between user and category"""
    __tablename__ = "interest"

    id = Column(Integer, primary_key = True)
    user = relationship("user", lazy = "joined")
    category = relationship("category", lazy = "joined")
