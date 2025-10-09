from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.get("/", response_model=List[schemas.UserRead])
def get_users(db: Session = Depends(get_db)):
    """
    Получить всех пользователей из базы данных
    """
    return db.query(models.user.User).all()


@router.post("/", response_model=schemas.UserRead)
def create_user(user_create: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Создать нового пользователя
    """
    existing_user = db.query(models.user.User).filter(models.user.User.username == user_create.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Имя пользователя уже существует!")

    new_user = models.user.User(username=user_create.username, is_admin=user_create.is_admin)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{user_id}", response_model=schemas.UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user