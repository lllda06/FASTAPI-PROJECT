from pydantic import BaseModel
from datetime import datetime

class SchemaCreateEvent(BaseModel):
    title: str
    description: str | None = None
    meeting_time: datetime

class SchemaEvent(BaseModel):
    id: int
    title: str
    description: str | None = None
    meeting_time: datetime

    class Config:
        from_attributes = True