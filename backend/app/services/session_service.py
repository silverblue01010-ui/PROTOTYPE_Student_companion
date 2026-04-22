from datetime import datetime
from bson import ObjectId
from app.database.db import session_collection
from app.models.session_model import session_helper


async def create_session(host_id: str, room_name: str) -> dict:
    doc = {
        "room_name": room_name,
        "host_id": host_id,
        "participants": [host_id],
        "is_active": True,
        "created_at": datetime.utcnow(),
    }
    result = await session_collection.insert_one(doc)
    created = await session_collection.find_one({"_id": result.inserted_id})
    return session_helper(created)


async def join_session(user_id: str, session_id: str) -> dict:
    await session_collection.update_one(
        {"_id": ObjectId(session_id)},
        {"$addToSet": {"participants": user_id}},
    )
    session = await session_collection.find_one({"_id": ObjectId(session_id)})
    return session_helper(session)


async def get_active_sessions() -> list:
    sessions = []
    async for s in session_collection.find({"is_active": True}):
        sessions.append(session_helper(s))
    return sessions


async def end_session(session_id: str) -> dict:
    await session_collection.update_one(
        {"_id": ObjectId(session_id)},
        {"$set": {"is_active": False}},
    )
    session = await session_collection.find_one({"_id": ObjectId(session_id)})
    return session_helper(session)