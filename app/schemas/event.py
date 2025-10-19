from pydantic import BaseModel
from datetime import datetime

class CreateEvent(BaseModel):
    title: str
    description: str
    meeting_time: datetime

class Event(BaseModel):
    id: int
    title: str
    description: str
    meeting_time: datetime

    class Config:
        from_attributes = True