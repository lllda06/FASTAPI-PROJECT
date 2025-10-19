from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.depends import get_db
from app.handlers.user_handler import UsersHandler
from app.schemas.user_schema import SchemaUser, SchemaCreateUser


router = APIRouter(prefix="/api/users", tags=["users"])


@router.get("", response_model=list[SchemaUser])
def list_users(skip: int = Query(0, ge=0), limit: int = Query(100, gt=0, le=500), db: Session = Depends(get_db)):
    return UsersHandler(db).list(skip, limit)


@router.get("/{user_id}", response_model=SchemaUser)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UsersHandler(db).get(user_id)


@router.post("", response_model=SchemaUser, status_code=201)
def create_user(payload: SchemaCreateUser, db: Session = Depends(get_db)):
    return UsersHandler(db).create(payload)