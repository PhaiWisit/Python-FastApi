from pydantic import BaseModel
import datetime


class ApplicantCreate(BaseModel):
    fullName: str
    age: int
    gender: str
    address: str
    email: str
    phone: str
    expectedSalary: int
    
class UserCreate(BaseModel):
    username: str
    password: str
    
class requestdetails(BaseModel):
    username:str
    password:str
        
class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class changepassword(BaseModel):
    email:str
    old_password:str
    new_password:str

class TokenCreate(BaseModel):
    user_id:str
    access_token:str
    refresh_token:str
    status:bool
    created_date:datetime.datetime       