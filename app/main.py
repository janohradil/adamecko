from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime

app = FastAPI()

# Static and template directories
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    current_year = datetime.now().year
    return templates.TemplateResponse("home.html", {"request": request, "year": current_year})

@app.get("/portfolio", response_class=HTMLResponse)
async def portfolio(request: Request):
    return templates.TemplateResponse("portfolio.html", {"request": request})

@app.get("/portfolio/items", response_class=HTMLResponse)
async def portfolio_items(request: Request):
    # Example portfolio data
    portfolio_data = [
        {"title": "Drevený stôl", "description": "Ručne zhotovený drevený jedálenský stôl."},
        {"title": "Kuchynské skrine", "description": "Na mieru zhotovené kuchynské skrine."},
        {"title": "Oltár", "description": "Oltárny stôl na liturgické účely."}
    ]
    return templates.TemplateResponse("partials/portfolio_items.html", {"request": request, "portfolio_data": portfolio_data})


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})
