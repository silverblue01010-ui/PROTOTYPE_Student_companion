from app.services.matching.filtering import filter_users
from app.services.matching.ranking import rank_users


def run_matching_pipeline(current_user: dict, all_users: list) -> list:
    candidates = filter_users(current_user, all_users)
    ranked = rank_users(current_user, candidates)
    return ranked