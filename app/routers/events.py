from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.depends import get_db
from app.handlers.event_handler import EventsHandler
from app.schemas.event_schema import SchemaEvent, SchemaCreateEvent


router = APIRouter(prefix="/api/events", tags=["events"])


@router.get("", response_model=list[SchemaEvent])
def get_events(skip: int = Query(0, ge=0), limit: int = Query(100, gt=0, le=500), db: Session = Depends(get_db)):
    return EventsHandler(db).list(skip, limit)


@router.post("", response_model=SchemaEvent, status_code=201)
def create_event(payload: SchemaCreateEvent, db: Session = Depends(get_db)):
    return EventsHandler(db).create(payload)