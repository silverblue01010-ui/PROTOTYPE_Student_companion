from app.services.matching.feature_engineering import extract_features


def jaccard(set_a: set, set_b: set) -> float:
    if not set_a and not set_b:
        return 0.0
    return len(set_a & set_b) / len(set_a | set_b)


def compute_similarity(user_a: dict, user_b: dict) -> float:
    fa = extract_features(user_a)
    fb = extract_features(user_b)

    skill_score = jaccard(fa["skills"], fb["skills"])
    interest_score = jaccard(fa["interests"], fb["interests"])

    # Weighted: skills 60%, interests 40%
    return round(0.6 * skill_score + 0.4 * interest_score, 4)