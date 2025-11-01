import os
from pymongo import MongoClient, errors

USE_MOCK_DB = os.getenv("USE_MOCK_DB", "false").lower() in ("1", "true", "yes")

if USE_MOCK_DB:
    import mongomock
    client = mongomock.MongoClient()
    # You may skip URI and timeouts because mock doesn’t need real server
    db = client.get_database("ship_rpg_mock_db")
    print("[db] Using mongomock in-memory database")
else:
    # real DB mode
    MONGO_URI = os.getenv(
        "MONGO_URI",
        "mongodb://admin:admin@192.168.1.14:27017/ship_rpg_db?authSource=admin"
    )
    TIMEOUT_MS = int(os.getenv("MONGO_TIMEOUT_MS", "5000"))

    client = MongoClient(
        MONGO_URI,
        serverSelectionTimeoutMS=TIMEOUT_MS,
        connectTimeoutMS=TIMEOUT_MS,
        socketTimeoutMS=TIMEOUT_MS
    )
    DB_NAME = os.getenv("MONGO_DBNAME", "ship_rpg_db")
    db = client.get_database(DB_NAME)
    print(f"[db] Connecting to MongoDB at {MONGO_URI}")

def check_connection() -> bool:
    if USE_MOCK_DB:
        # mock always “connected”
        return True
    try:
        client.admin.command("ping")
        return True
    except errors.PyMongoError as e:
        print(f"[db] check_connection failed: {e}")
        return False

class BaseModel:
    collection_name = None

    @classmethod
    def collection(cls):
        return db[cls.collection_name]

    def save(self):
        data = self.to_dict()
        result = self.collection().insert_one(data)
        return result.inserted_id

    @classmethod
    def find_one(cls, filter_dict):
        data = cls.collection().find_one(filter_dict)
        if data:
            return cls.from_dict(data)
        return None

    def to_dict(self):
        raise NotImplementedError

    @classmethod
    def from_dict(cls, data):
        raise NotImplementedError