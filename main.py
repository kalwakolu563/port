from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models import Lead
from database import engine, create_table

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

create_table()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/projects", response_class=HTMLResponse)
def projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.post("/submit", response_class=HTMLResponse)
async def submit_form(name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    with engine.connect() as conn:
        conn.execute(Lead.__table__.insert().values(name=name, email=email, message=message))
    return RedirectResponse("/", status_code=302)
