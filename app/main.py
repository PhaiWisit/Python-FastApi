import os
from fastapi import FastAPI, Request
from app.database.database import Base, engine
from app.api import applicants,exportCsv,auth
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(engine)
    
app = FastAPI()
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
app.include_router(applicants.router)
app.include_router(exportCsv.router)
app.include_router(auth.router,prefix="/auth")
