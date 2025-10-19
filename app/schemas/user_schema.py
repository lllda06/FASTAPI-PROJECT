from datetime import datetime
from pydantic import BaseModel, EmailStr


class SchemaCreateUser(BaseModel):
    email: str
    full_name: str | None = None


class SchemaUser(BaseModel):
    id: int
    email: str
    full_name: str | None = None
    created_at: datetime


    class Config:
        from_attributes = True