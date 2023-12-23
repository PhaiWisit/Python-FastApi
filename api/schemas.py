from pydantic import BaseModel

class ApplicantCreate(BaseModel):
    fullName: str
    age: int
    gender: str
    address: str
    email: str
    phone: str
    expectedSalary: int
    