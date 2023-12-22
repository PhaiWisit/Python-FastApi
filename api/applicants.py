from sqlalchemy.orm import Session
from database import Base, engine, Applicants
from fastapi import FastAPI,status,APIRouter, HTTPException, Path
from api.models import ApplicantSchema

router = APIRouter()

@router.post("/applicant", status_code=status.HTTP_201_CREATED)
def create_applicant(payload: ApplicantSchema):
    
    session = Session(bind=engine, expire_on_commit=False)
    applicantDb = Applicants(fullName = payload.fullName)
    session.add(applicantDb)
    session.commit()
    id = applicantDb.id
    session.close()
    
    return f"created applicant with id {id}"


@router.get("/applicant/{id}")
def read_applicant(id: int):
    
    session = Session(bind=engine, expire_on_commit=False)
    applicant = session.query(Applicants).get(id)
    session.close()
    
    if not applicant:
        raise HTTPException(status_code=404, detail=f"applicant with id {id} not found")
    
    return applicant


@router.get("/applicant")
def read_applicant_list():
    
    session = Session(bind=engine, expire_on_commit=False)
    applicant_list = session.query(Applicants).all()
    session.close()

    return applicant_list


@router.put("/applicant/{id}")
def update_applicant(id: int, payload: ApplicantSchema):

    session = Session(bind=engine, expire_on_commit=False)
    applicant = session.query(Applicants).get(id)

    if applicant:
        applicant.fullName = payload.fullName
        session.commit()
    session.close()

    if not applicant:
        raise HTTPException(status_code=404, detail=f"applicant with id {id} not found")

    return applicant


@router.delete("/applicant/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_applicant(id: int):

    session = Session(bind=engine, expire_on_commit=False)
    applicant = session.query(Applicants).get(id)

    if applicant:
        session.delete(applicant)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return None