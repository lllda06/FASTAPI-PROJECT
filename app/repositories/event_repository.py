from sqlalchemy.orm import Session
from app.database.models import EventModel
from app.dto.event_dto import CreateEventDTO, EventDTO

class EventRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def list(self, skip: int = 0, limit: int = 100) -> list[EventDTO]:
        rows = (
            self.db.query(EventModel)
            .order_by(EventModel.meeting_time.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )
        return [EventDTO.model_validate(r, from_attributes=True) for r in rows]

    def create(self, data: CreateEventDTO) -> EventDTO:
        row = EventModel(
            title=data.title,
            description=data.description,
            meeting_time=data.meeting_time,
        )
        self.db.add(row)
        self.db.commit()
        self.db.refresh(row)
        return EventDTO.model_validate(row, from_attributes=True)