from sqlalchemy import  Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database.database import Base

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