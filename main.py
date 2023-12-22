from fastapi import FastAPI
from database import Base, engine
from api import applicants

    
Base.metadata.create_all(engine)
    
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Applicants"}

app.include_router(applicants.router)

