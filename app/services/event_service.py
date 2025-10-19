from sqlalchemy.orm import Session
from app.dto.event_dto import CreateEventDTO, EventDTO
from app.repositories.event_repository import EventRepository

class EventService:
    def __init__(self, repo: EventRepository) -> None:
        self.repo = repo

    @classmethod
    def from_session(cls, db: Session) -> "EventService":
        return cls(EventRepository(db))

    def list_events(self, skip:int=0, limit:int=100) -> list[EventDTO]:
        return self.repo.list(skip=skip, limit=limit)

    def create_event(self, data: CreateEventDTO) -> EventDTO:
        return self.repo.create(data)
