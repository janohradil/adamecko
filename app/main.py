from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime

app = FastAPI()

# Static and template directories
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Dependency to provide the current year
def get_year():
    """Return the current year as a dictionary."""
    current_year = datetime.now().year
    return {"year": current_year}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, current_year: dict = Depends(get_year)):
    return templates.TemplateResponse("home.html", {"request": request, **current_year})

@app.get("/portfolio", response_class=HTMLResponse)
async def portfolio_view(request: Request, current_year: dict = Depends(get_year)):
    """Return the portfolio page."""
    return templates.TemplateResponse("portfolio.html", {"request": request, **current_year})

@app.get("/portfolio/items", response_class=HTMLResponse)
async def portfolio_items(request: Request, current_year: dict = Depends(get_year)):
    # Example portfolio data
    """
    Return the portfolio items page.

    The page displays a list of portfolio items, including images and descriptions.

    The data is currently hard-coded for demonstration purposes. In the future, it
    should be replaced with a database query.
    """
    portfolio_data = [
        {"title": "Drevený stôl", "description": "Ručne zhotovený drevený jedálenský stôl."},
        {"title": "Kuchynské skrine", "description": "Na mieru zhotovené kuchynské skrine."},
        {"title": "Oltár", "description": "Oltárny stôl na liturgické účely."}
    ]
    return templates.TemplateResponse("partials/portfolio_items.html", {"request": request, "portfolio_data": portfolio_data, **current_year})


@app.get("/kontakt", response_class=HTMLResponse)
async def contact_view(request: Request, current_year: dict = Depends(get_year)):
    """Return the contact page."""
    return templates.TemplateResponse("kontakt.html", {"request": request, **current_year})
