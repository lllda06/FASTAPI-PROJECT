from pydantic import BaseModel
from datetime import datetime

class CreateEventDTO(BaseModel):
    title: str
    description: str | None = None
    meeting_time: datetime

class EventDTO(BaseModel):
    id: int
    title: str
    description: str | None = None
    meeting_time: datetime