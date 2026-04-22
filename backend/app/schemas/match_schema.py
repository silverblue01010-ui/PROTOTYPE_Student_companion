from pydantic import BaseModel
from typing import List


class MatchResult(BaseModel):
    id: str
    name: str
    email: str
    skills: List[str]
    interests: List[str]
    bio: str
    score: float