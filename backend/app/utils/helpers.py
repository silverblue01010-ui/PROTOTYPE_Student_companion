from bson import ObjectId


def is_valid_object_id(oid: str) -> bool:
    try:
        ObjectId(oid)
        return True
    except Exception:
        return False