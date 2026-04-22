from bson import ObjectId

def session_helper(session) -> dict:
    return {
        "id": str(session["_id"]),
        "room_name": session["room_name"],
        "host_id": session["host_id"],
        "participants": session.get("participants", []),
        "is_active": session.get("is_active", True)
    }