from fastapi import APIRouter, HTTPException, Depends
from bson import ObjectId

from app.database.db import user_collection
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse, TokenResponse
from app.core.security import hash_password, verify_password, create_access_token
from app.core.dependencies import get_current_user
from app.models.user_model import user_helper

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=201)
async def register(user: UserCreate):
    existing = await user_collection.find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed = hash_password(user.password)
    user_doc = {
        "name": user.name,
        "email": user.email,
        "password": hashed,
        "skills": user.skills or [],
        "interests": user.interests or [],
        "bio": user.bio or "",
    }
    result = await user_collection.insert_one(user_doc)
    created = await user_collection.find_one({"_id": result.inserted_id})
    return user_helper(created)


@router.post("/login", response_model=TokenResponse)
async def login(credentials: UserLogin):
    user = await user_collection.find_one({"email": credentials.email})
    if not user or not verify_password(credentials.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"user_id": str(user["_id"])})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me", response_model=UserResponse)
async def get_me(user_id: str = Depends(get_current_user)):
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user_helper(user)


@router.get("/", response_model=list[UserResponse])
async def get_all_users():
    users = []
    async for user in user_collection.find():
        users.append(user_helper(user))
    return users


@router.put("/me")
async def update_profile(updates: dict, user_id: str = Depends(get_current_user)):
    # Prevent updating sensitive fields
    updates.pop("password", None)
    updates.pop("email", None)
    await user_collection.update_one({"_id": ObjectId(user_id)}, {"$set": updates})
    updated = await user_collection.find_one({"_id": ObjectId(user_id)})
    return user_helper(updated)