# src/tests/conftest.py

import os
import pytest
from src.game.db import db, USE_MOCK_DB

@pytest.fixture(autouse=True)
def clear_db():
    """
    Clear all collections before each test when using the mock DB.
    If real DB is used, only clear if configured accordingly.
    """
    if USE_MOCK_DB:
        for col in db.list_collection_names():
            db.drop_collection(col)
    yield
    if USE_MOCK_DB:
        for col in db.list_collection_names():
            db.drop_collection(col)