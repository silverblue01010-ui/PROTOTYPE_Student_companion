from bson import ObjectId
from app.database.db import user_collection
from app.models.user_model import user_helper


async def get_user_by_id(user_id: str) -> dict | None:
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    return user_helper(user) if user else None