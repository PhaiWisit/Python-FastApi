from fastapi import FastAPI
from database import Base, engine,Applicants
from api import applicants,exportCsv
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)
    
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Applicants"}

app.include_router(applicants.router)
app.include_router(exportCsv.router)
