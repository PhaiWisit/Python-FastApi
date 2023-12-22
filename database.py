from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

# Create a sqlite engine instance
engine = create_engine("sqlite:///applyjob.db")

# Create a DeclarativeMeta instance
Base = declarative_base()

# Define To Do class inheriting from Base
class Applicants(Base):
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
    
