from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/api/events", tags=["Events"])


@router.post("/", response_model=schemas.event.EventRead)
def create_event(event_create: schemas.event.EventCreate, db: Session = Depends(get_db)):
    """
    Создать новое событие
    """
    event = models.event.Event(
        title=event_create.title,
        description=event_create.description,
        meeting_time=event_create.meeting_time
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


@router.get("/", response_model=List[schemas.event.EventRead])
def get_upcoming_events(db: Session = Depends(get_db)):
    """
    Получить все события, которые ещё не начались
    """
    now = datetime.now()
    events = db.query(models.event.Event).filter(models.event.Event.meeting_time > now).all()
    return events


@router.post("/{event_id}/subscribe")
def subscribe_to_event(event_id: int, user_id: int, db: Session = Depends(get_db)):
    """
    Подписать пользователя на событие (если оно ещё не началось)
    """
    event = db.query(models.event.Event).filter(models.event.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Событие не найдено")

    if event.meeting_time <= datetime.now():
        raise HTTPException(status_code=400, detail="Нельзя подписаться на уже начавшееся событие")

    user = db.query(models.user.User).filter(models.user.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    if user in event.participants:
        raise HTTPException(status_code=400, detail="Пользователь уже подписан на это событие")

    event.participants.append(user)
    db.commit()
    return {"message": f"Пользователь {user.username} подписан на событие '{event.title}'"}


@router.get("/user/{user_id}", response_model=List[schemas.event.EventRead])
def get_user_events(user_id: int, db: Session = Depends(get_db)):
    """
    Получить все события, на которые подписан пользователь
    """
    user = db.query(models.user.User).filter(models.user.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user.events
