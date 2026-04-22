from app.database.db import user_collection
from app.services.matching.pipeline import run_matching_pipeline
from app.models.user_model import user_helper


async def get_matches_for_user(current_user: dict) -> list:
    all_users = []
    async for user in user_collection.find():
        all_users.append(user)

    results = run_matching_pipeline(current_user, all_users)

    formatted = []
    for u in results:
        h = user_helper(u)
        h["score"] = u.get("score", 0)
        formatted.append(h)
    return formatted