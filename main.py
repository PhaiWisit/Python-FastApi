from fastapi import FastAPI, Request
from database import Base, engine
from api import applicants
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


templates = Jinja2Templates(directory="templates")


@app.get("/")
@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello Applicants"})
app.include_router(applicants.router)
app.include_router(exportCsv.router)
