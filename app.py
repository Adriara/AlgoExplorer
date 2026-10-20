from fastapi import APIRouter
from fastapi.responses import HTMLResponse

# Create an isolated router for this specific sub-project
router = APIRouter()

@router.get("/")
async def inventory_home():
    """
    This handles the main landing route for the inventory sub-project.
    When a user visits /inventory/, this HTML response will trigger.
    """
    html_content = """
    <html>
        <head>
            <title>My Inventory App</title>
            <style>
                body { font-family: sans-serif; background: #f4f6f9; text-align: center; padding: 50px; }
                .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); display: inline-block; }
                h1 { color: #2c3e50; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>📦 Welcome to My Inventory Sub-Project!</h1>
                <p>This app is running isolated inside your SaaS infrastructure.</p>
                <a href="/">← Go Back to Main Site</a>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@router.get("/items")
async def get_items():
    """An example of a secondary route inside your sub-project: /inventory/items"""
    return {"items": ["Item A", "Item B", "Item C"]}
