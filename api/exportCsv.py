from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import io
import pandas as pd
from datetime import datetime

from sqlalchemy.orm import Session
from database import Base, engine, Applicants

router = APIRouter()

@router.get("/get_csv")
async def get_csv():
    
    session = Session(bind=engine, expire_on_commit=False)
    applicant_list = session.query(Applicants).all()
    session.close()
   
    df = pd.DataFrame([(applicant.id, applicant.fullName, applicant.gender,
                        applicant.age, applicant.address, applicant.email,
                        applicant.phone, applicant.expectedSalary,
                        applicant.createdDate) for applicant in applicant_list],
                      columns=["id", "fullName", "gender", "age", "address",
                               "email", "phone", "expectedSalary", "createdDate"])

    stream = io.StringIO()
    df.to_csv(stream, index=False)

    filename = f"Applicants List-{datetime.now().strftime('%d%m%y-%H%M%S')}.csv"
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"

    return response
