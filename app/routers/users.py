from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import CreateUser, User
from app.dto.user_dto import UserCreateDTO, UserResponseDTO
from app.services.user_service import register_user, get_users, get_user
from depends import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/api/users", response_model=UserResponseDTO)
async def create_user(user: UserCreateDTO, db: Session = Depends(get_db)):
    return await register_user(user, db)

@router.get("/api/users", response_model=list[UserResponseDTO])
async def get_users_list(db: Session = Depends(get_db)):
    users = await get_users(db)
    return users

@router.get("/api/users/{user_id}", response_model=UserResponseDTO)
async def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return await get_user(user_id, db)