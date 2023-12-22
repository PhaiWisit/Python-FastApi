from pydantic import BaseModel

class ApplicantSchema(BaseModel):
    fullName: str