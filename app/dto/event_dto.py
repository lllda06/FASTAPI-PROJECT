from pydantic import BaseModel
from datetime import datetime

class CreateEventDTO(BaseModel):
    title: str
    description: str
    meeting_time: datetime

class EventResponseDTO(BaseModel):
    id: int
    title: str
    description: str
    meeting_time: datetime

    class Config:
        orm_mode = True