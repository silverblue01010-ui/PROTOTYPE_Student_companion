from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId

from app.core.dependencies import get_current_user
from app.database.db import user_collection
from app.services.match_service import get_matches_for_user

router = APIRouter()


@router.get("/")
async def get_matches(user_id: str = Depends(get_current_user)):
    """Return ranked match list for the authenticated user."""
    current_user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")

    matches = await get_matches_for_user(current_user)
    return {"matches": matches}