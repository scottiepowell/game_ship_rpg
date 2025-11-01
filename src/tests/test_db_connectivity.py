import pytest
from src.game.db import check_connection

def test_db_reachable():
    assert check_connection(), "Database should be reachable for integration tests."