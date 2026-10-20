import os
import sys
from pathlib import Path
import uvicorn

# 1. Force find the exact folder containing this run.py file
current_file_path = Path(__file__).resolve()
project_root = current_file_path.parent

# 2. Inject the root into both sys.path AND the OS environment variables
sys.path.insert(0, str(project_root))
os.environ["PYTHONPATH"] = str(project_root)

# 3. Perform the import safely AFTER the paths are locked into the system environment
try:
    from apps.main_platform.app import app
except ModuleNotFoundError:
    # Fallback pathing injection if Python 3.14 strict mode is engaged
    sys.path.append(str(project_root / "apps"))
    from main_platform.app import app

if __name__ == "__main__":
    uvicorn.run(
        app, 
        host="127.0.0.1", 
        port=8000, 
        reload=False  # Keep reload off temporarily to bypass multi-process spawning bugs
    )
