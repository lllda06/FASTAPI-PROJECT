from sqlalchemy.orm import Session
from app.schemas.user import User, CreateUser

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db:Session, user_data: CreateUser):
    db_user = User(username=user_data.username, email=user_data.email, first_name=user_data.first_name, last_name=user_data.last_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()