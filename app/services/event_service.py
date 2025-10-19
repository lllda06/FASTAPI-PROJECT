from sqlalchemy.orm import Session
from app.dto.event_dto import EventResponseDTO, CreateEventDTO
from app.schemas.event import Event, CreateEvent

def create_event(event_data: CreateEvent, db: Session):
    db_event = EventModel(title=event_data.title, description=event_data.description, meeting_time=event_data.meeting_time)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return Event.from_orm(db_event)

def get_events(db: Session):
    return db.query(Event).all()
