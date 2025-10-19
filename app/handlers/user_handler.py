from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.services.user_service import UserService
from app.dto.user_dto import CreateUserDTO
from app.schemas.user_schema import SchemaUser, SchemaCreateUser
from app.exceptions import NotFoundError, ConflictError


class UsersHandler:
    def __init__(self, db: Session) -> None:
        self.svc = UserService.from_session(db)

    def list(self, skip: int, limit: int) -> list[SchemaUser]:
        dtos = self.svc.list_users(skip, limit)
        return [SchemaUser.model_validate(d) for d in dtos]

    def get(self, user_id: int) -> SchemaUser:
        dto = self.svc.get_user(user_id)
        return SchemaUser.model_validate(dto)


    def create(self, payload: SchemaCreateUser) -> SchemaUser:
        dto = self.svc.create_user(CreateUserDTO(**payload.model_dump()))
        if dto is None:
            raise HTTPException(status_code=400, detail="Failed to create user")
        return SchemaUser.model_validate(dto)