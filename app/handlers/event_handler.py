from app.repository.event_repository import create_event, get_events
from app.schemas.event import CreateEvent, Event
from sqlalchemy.orm import Session

def create_event_handler(event: CreateEvent, db: Session):
    return create_event(db, event)

def get_events_handler(db: Session):
    return get_events(db)