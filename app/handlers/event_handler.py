from sqlalchemy.orm import Session
from app.services.event_service import EventService
from app.dto.event_dto import CreateEventDTO
from app.schemas.event_schema import SchemaEvent, SchemaCreateEvent


class EventsHandler:
    def __init__(self, db: Session) -> None:
        self.svc = EventService.from_session(db)


    def list(self, skip: int, limit: int) -> list[SchemaEvent]:
        dtos = self.svc.list_events(skip, limit)
        return [SchemaEvent.model_validate(d) for d in dtos]


    def create(self, payload: SchemaCreateEvent) -> SchemaEvent:
        dto = self.svc.create_event(CreateEventDTO(**payload.model_dump()))
        return SchemaEvent.model_validate(dto)