from pydantic import BaseModel

class UserCreateDTO(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str

class UserResponseDTO(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool

    class Config:
        orm_mode = True