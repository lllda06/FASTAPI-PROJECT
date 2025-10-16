from app.repository.user_repository import create_user, get_users
from app.schemas.user import CreateUser, User
from sqlalchemy.orm import Session

def create_user_handler(user: CreateUser, db: Session):
    return create_user(db, user)

def get_users_handler(db: Session):
    return get_users(db)