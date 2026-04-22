from app.services.matching.similarity import compute_similarity
from app.core.constants import MAX_MATCHES, MIN_SIMILARITY_SCORE


def rank_users(current_user: dict, candidates: list) -> list:
    scored = []
    for candidate in candidates:
        score = compute_similarity(current_user, candidate)
        if score >= MIN_SIMILARITY_SCORE:
            scored.append({**candidate, "score": score})

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:MAX_MATCHES]