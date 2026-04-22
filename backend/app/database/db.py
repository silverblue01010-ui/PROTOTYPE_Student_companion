from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(settings.MONGO_URL)

database = client[settings.DB_NAME]

user_collection = database.get_collection("users")
match_collection = database.get_collection("matches")
session_collection = database.get_collection("sessions")