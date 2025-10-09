from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    is_admin = Column(Boolean, default=False)

    # События, на которые подписан пользователь
    events = relationship("Event", secondary="subscriptions", back_populates="participants")