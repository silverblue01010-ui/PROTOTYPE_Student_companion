from fastapi import APIRouter, Depends

from app.core.dependencies import get_current_user
from app.services.session_service import (
    create_session,
    join_session,
    get_active_sessions,
    end_session,
)

router = APIRouter()


@router.post("/create")
async def create(room_name: str, user_id: str = Depends(get_current_user)):
    return await create_session(user_id, room_name)


@router.post("/join")
async def join(session_id: str, user_id: str = Depends(get_current_user)):
    return await join_session(user_id, session_id)


@router.get("/active")
async def active_sessions():
    return await get_active_sessions()


@router.post("/end")
async def end(session_id: str, user_id: str = Depends(get_current_user)):
    return await end_session(session_id)