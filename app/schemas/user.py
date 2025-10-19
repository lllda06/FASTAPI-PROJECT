from pydantic import BaseModel
from datetime import datetime

class CreateUser(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str

class User(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool

    class Config:
        from_attributes = True