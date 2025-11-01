#!/usr/bin/env bash
set -e

# Avoid .pyc bytecode clutter
export PYTHONDONTWRITEBYTECODE=1

# Use mongomock
export USE_MOCK_DB=true

echo "[Codex] Initializing virtualenv..."
python3 -m venv venv
source venv/bin/activate

echo "[Codex] Upgrading pip..."
pip install --upgrade pip

echo "[Codex] Installing dependencies..."
pip install -r requirements.txt --no-cache-dir

# Useful for linting & formatting within Codex
pip install pytest flake8 black --no-cache-dir

# Use a default test MongoDB URI for test runs
export MONGO_URI="mongodb://localhost:27017/ship_rpg_test"

echo "[Codex] Running DB connection check..."
python3 - << 'PYCODE'
from src.game.db import check_connection
import sys
if not check_connection():
    sys.exit("[Codex] ERROR: DB connection failed")
print("[Codex] DB connection check passed")
PYCODE

echo "[Codex] Environment ready."