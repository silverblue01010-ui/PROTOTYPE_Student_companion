def filter_users(current_user: dict, all_users: list) -> list:
    """Remove the current user from the candidate pool."""
    current_id = str(current_user.get("_id", current_user.get("id", "")))
    return [
        u for u in all_users
        if str(u.get("_id", u.get("id", ""))) != current_id
    ]