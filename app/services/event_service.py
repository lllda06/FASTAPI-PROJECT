from app.handlers.event_handler import create_event_handler, get_events_handler
from app.dto.event_dto import CreateEventDTO, EventResponseDTO
from sqlalchemy.orm import Session

def create_event(event: CreateEventDTO, db: Session):
    return create_event_handler(event, db)

def get_events(db: Session):
    return get_events_handler(db)