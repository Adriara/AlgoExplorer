from fastapi import APIRouter
from fastapi.responses import HTMLResponse

# Create an isolated router just for the inventory app tool
router = APIRouter()

@router.get("/")
async def inventory_home():
    html_content = """
    <html>
        <head><title>My Inventory App</title></head>
        <body style="font-family: sans-serif; text-align: center; padding: 50px; background: #f4f6f9;">
            <h1>📦 Welcome to My Inventory Sub-Project!</h1>
            <p>This tool is running isolated within your modular infrastructure.</p>
            <a href="/">← Go Back to Main Site</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
