from fastapi import APIRouter, Depends, HTTPException

from app.dto.event_dto import EventResponseDTO, CreateEventDTO
from app.schemas.event import CreateEvent, Event
from app.services.event_service import create_event, get_events
from depends import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/api/events", response_model=EventResponseDTO)
async def create_event_view(event: CreateEventDTO, db: Session = Depends(get_db)):
    return await create_event(event, db)

@router.get("/api/events", response_model=list[EventResponseDTO])
async def get_events_list(db: Session = Depends(get_db)):
    events = await get_events(db)
    return events