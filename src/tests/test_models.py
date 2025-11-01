import pytest
import os
from game.db import db
from game.models import Player

@pytest.fixture(autouse=True)
def clear_db():
    db.players.delete_many({})
    yield
    db.players.delete_many({})

def test_player_level_up_resets_experience():
    player = Player("TestHero")
    inserted_id = player.save()
    player.experience = 123
    player.level_up()
    reloaded = Player.find_one({"name": "TestHero"})
    assert reloaded.level == 2
    assert reloaded.experience == 0