#!/bin/bash
# Go up one directory to the project root
# cd "$(dirname "${BASH_SOURCE[0]}")/.."

echo "Current directory: $(pwd)"

# Activate the virtual environment
# source backend/venv/bin/activate
source venv/bin/activate

# Now, uvicorn can find backend.src.main as a module
# uvicorn backend.src.main:app --reload --host 0.0.0.0 --port 8000 --log-config=backend/logging.ini 
uvicorn main:app --reload --host 0.0.0.0 --port 8000 --log-config=logging.ini --reload-dir src --app-dir src
