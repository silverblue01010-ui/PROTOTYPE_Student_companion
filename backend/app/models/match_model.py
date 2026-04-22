from datetime import datetime


def match_model(user_id: str, matches: list):
    return {
        "user_id": user_id,
        "matches": matches,
        "created_at": datetime.utcnow()
    }