from pydantic import BaseModel, EmailStr
from typing import List, Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    skills: Optional[List[str]] = []
    interests: Optional[List[str]] = []
    bio: Optional[str] = ""


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    skills: List[str]
    interests: List[str]
    bio: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"