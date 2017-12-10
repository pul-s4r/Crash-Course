from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_login import UserMixin

db_string = "sqlite:///crash_course.db"
engine = create_engine(db_string)

Base = declarative_base()

try:
    Base.metadata.create_all(engine)
except:
    pass

Base.metadata.bind = engine
Session = sessionmaker(bind = engine)

class User(Base, UserMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key = True)
    username = Column(String, nullable = False, unique = True)
    fname = Column(String, nullable = False)
    lname = Column(String, nullable = False)

class Password(Base):
    __tablename__ = "password"

    id = Column(Integer, primary_key = True)
    val = Column(String, nullable = False)
