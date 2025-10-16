from sqlalchemy.orm import Session
from app.schemas.event import Event, CreateEvent

def get_events(db:Session, skip: int = 0, limit: int = 100):
    return db.query(Event).offset(skip).limit(limit).all()

def  create_event(db:Session, event_data: CreateEvent):
    db_event = Event(title=event_data.title, description=event_data.description, meeting_time=event_data.meeting_time)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event