from datetime import datetime
from sqlalchemy import String, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database.session import Base

class EventModel(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column( primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(Text(), nullable=True)
    meeting_time: Mapped[datetime] = mapped_column(DateTime(timezone=False))

class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column( primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    full_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=False), server_default=func.now())
