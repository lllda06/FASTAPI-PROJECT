from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


# Таблица связи пользователей и событий (подписки)
subscriptions = Table(
    "subscriptions",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("event_id", Integer, ForeignKey("events.id"))
)


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    meeting_time = Column(DateTime, nullable=False)

    # Подписчики события
    participants = relationship("User", secondary=subscriptions, back_populates="events")
