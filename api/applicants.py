from sqlalchemy.orm import Session
from database.database import engine
from database.models import  Applicant
from fastapi import status,APIRouter, HTTPException, Path
from api.schemas import ApplicantCreate


router = APIRouter()

@router.post("/applicant", status_code=status.HTTP_201_CREATED)
def create_applicant(payload: ApplicantCreate):
    
    session = Session(bind=engine, expire_on_commit=False)
    new_applicant = Applicant(
        fullName = payload.fullName,
        age = payload.age,
        gender = payload.gender,
        address = payload.address,
        email = payload.email,
        phone = payload.phone,
        expectedSalary = payload.expectedSalary )
    session.add(new_applicant)
    session.commit()
    id = new_applicant.id
    session.close()
    
    return f"created applicant with id {id}"


@router.get("/applicant/{id}")
def read_applicant(id: int):
    
    session = Session(bind=engine, expire_on_commit=False)
    applicant = session.query(Applicant).get(id)
    session.close()
    
    if not applicant:
        raise HTTPException(status_code=404, detail=f"applicant with id {id} not found")
    
    return applicant


@router.get("/applicant")
def read_applicant_list():
    
    session = Session(bind=engine, expire_on_commit=False)
    applicant_list = session.query(Applicant).all()
    session.close()

    return applicant_list


@router.put("/applicant/{id}")
def update_applicant(id: int, payload: ApplicantCreate):

    session = Session(bind=engine, expire_on_commit=False)
    applicant = session.query(Applicant).get(id)

    if applicant:
        applicant.fullName = payload.fullName
        applicant.age = payload.age
        applicant.gender = payload.gender
        applicant.address = payload.address
        applicant.email = payload.email
        applicant.phone = payload.phone
        applicant.expectedSalary = payload.expectedSalary
        session.commit()
    session.close()

    if not applicant:
        raise HTTPException(status_code=404, detail=f"applicant with id {id} not found")

    return applicant


@router.delete("/applicant/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_applicant(id: int):

    session = Session(bind=engine, expire_on_commit=False)
    applicant = session.query(Applicant).get(id)

    if applicant:
        session.delete(applicant)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return None

