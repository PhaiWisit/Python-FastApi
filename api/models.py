from pydantic import BaseModel

class ApplicantModel(BaseModel):
    fullName: str
    age: int
    gender: str
    address: str
    email: str
    phone: str
    expectedSalary: int
    