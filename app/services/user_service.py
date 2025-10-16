from app.repository.user_repository import get_user_by_id
from app.dto.user_dto import UserCreateDTO, UserResponseDTO
from sqlalchemy.orm import Session
from fastapi import HTTPException

def register_user(user: UserCreateDTO, db: Session):
    pass

def get_users(db: Session):
    pass

def get_user(user_id: int, db: Session):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user