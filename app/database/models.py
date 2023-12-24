from sqlalchemy import  Column, Integer, String, DateTime,Boolean
from sqlalchemy.sql import func
from app.database.database import Base
import datetime


class Applicant(Base):
    __tablename__ = 'applicants'
    id = Column(Integer, primary_key=True)
    fullName = Column(String(256))
    gender = Column(String(256))
    age = Column(Integer)
    address = Column(String(256))
    email = Column(String(256))
    phone = Column(String(256))
    expectedSalary = Column(Integer)
    createdDate = Column(DateTime, default=func.now(), nullable=False)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    username = Column(String(50))
    password = Column(String(100))
    
class TokenTable(Base):
    __tablename__ = "token"
    user_id = Column(Integer)
    access_toke = Column(String(450), primary_key=True)
    refresh_toke = Column(String(450),nullable=False)
    status = Column(Boolean)
    created_date = Column(DateTime, default=datetime.datetime.now)    