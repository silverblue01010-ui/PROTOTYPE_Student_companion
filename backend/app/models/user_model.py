from bson import ObjectId


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user.get("name", ""),
        "email": user.get("email", ""),
        "skills": user.get("skills", []),
        "interests": user.get("interests", []),
        "bio": user.get("bio", ""),
    }