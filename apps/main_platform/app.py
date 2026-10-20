import sys
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# 1. Establish precise parent folder navigation parameters
root_path = Path(__file__).resolve().parent.parent.parent
if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

from apps.my_inventory.app import router as inventory_router

app = FastAPI(title="My SaaS Platform Master")

# 2. Point directly to the templates folder
CURRENT_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(CURRENT_DIR / "templates"))

@app.get("/", response_class=HTMLResponse)
async def main_homepage(request: Request):
    # 3. FIXED LINE: Pass 'request' as the very first positional parameter
    return templates.TemplateResponse(request, "index.html")

app.include_router(inventory_router, prefix="/inventory")
