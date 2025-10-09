from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    is_admin: bool = False


class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True