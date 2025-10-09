from pydantic import BaseModel
from datetime import datetime
from typing import List


class EventBase(BaseModel):
    title: str
    description: str | None = None
    meeting_time: datetime


class EventCreate(EventBase):
    pass


class EventRead(EventBase):
    id: int

    class Config:
        orm_mode = True


class EventWithParticipants(EventRead):
    participants: List[str]
