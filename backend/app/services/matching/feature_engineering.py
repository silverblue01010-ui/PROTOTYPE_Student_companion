def extract_features(user: dict) -> dict:
    return {
        "skills": set(s.lower() for s in user.get("skills", [])),
        "interests": set(i.lower() for i in user.get("interests", [])),
    }