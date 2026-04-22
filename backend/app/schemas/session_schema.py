from pydantic import BaseModel
from typing import List

class SessionCreate(BaseModel):
    room_name: str

class SessionResponse(BaseModel):
    id: str
    room_name: str
    host_id: str
    participants: List[str]
    is_active: bool