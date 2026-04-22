# Placeholder for future activity tracking (e.g., last seen, sessions joined)
from datetime import datetime
from app.database.db import user_collection
from bson import ObjectId


async def update_last_seen(user_id: str):
    await user_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"last_seen": datetime.utcnow()}},
    )