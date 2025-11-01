import os
from pymongo import MongoClient, errors

# Connection URI including default database name
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://admin:admin@192.168.1.14:27017/ship_rpg_db?authSource=admin"
)

# Timeout values (in milliseconds)
TIMEOUT_MS = int(os.getenv("MONGO_TIMEOUT_MS", "5000"))  # default to 5 seconds

# Create client with timeout so it fails fast if cannot connect
client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=TIMEOUT_MS,
    connectTimeoutMS=TIMEOUT_MS,
    socketTimeoutMS=TIMEOUT_MS
)

# Explicitly pick the database by name
DB_NAME = os.getenv("MONGO_DBNAME", "ship_rpg_db")
db = client.get_database(DB_NAME)

def check_connection() -> bool:
    try:
        # Send ping command to confirm connection
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