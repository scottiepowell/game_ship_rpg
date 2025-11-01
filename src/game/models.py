from .db import BaseModel

class Player(BaseModel):
    collection_name = "players"

    def __init__(self, name, level=1, experience=0, current_location="bridge", ship_id=None):
        self.name = name
        self.level = level
        self.experience = experience
        self.current_location = current_location
        self.ship_id = ship_id

    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "experience": self.experience,
            "current_location": self.current_location,
            "ship_id": self.ship_id,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            level=data["level"],
            experience=data["experience"],
            current_location=data.get("current_location"),
            ship_id=data.get("ship_id"),
        )

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.collection().update_one(
            {"name": self.name},
            {"$set": {"level": self.level, "experience": self.experience}}
        )