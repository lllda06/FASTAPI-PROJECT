from fastapi import APIRouter, Depends
from app.dto.event_dto import EventResponseDTO, CreateEventDTO
from app.schemas.event import CreateEvent, Event
from app.services.event_service import create_event, get_events
from depends import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/api/events", response_model=EventResponseDTO)
def create_event_view(event: CreateEventDTO, db: Session = Depends(get_db)):
    # Теперь функция create_event не асинхронная
    return create_event(event, db)

@router.get("/api/events", response_model=list[EventResponseDTO])
def get_events_list(db: Session = Depends(get_db)):
    events = get_events(db)
    return events