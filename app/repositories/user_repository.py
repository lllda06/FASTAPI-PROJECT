from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database.models import UserModel
from app.dto.user_dto import CreateUserDTO, UserDTO
from app.exceptions import NotFoundError, ConflictError


class UserRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def user_get(self, user_id:int):
        row = self.db.get(UserModel, user_id)
        if row:
            return UserDTO.model_validate(row, from_attributes=True)
        else:
            raise NotFoundError("User not found")

    def users_list(self, skip: int = 0, limit: int = 100):
        rows = (
            self.db.query(UserModel)
            .order_by(UserModel.id.asc())
            .offset(skip)
            .limit(limit)
            .all()
        )
        return [UserDTO.model_validate(r, from_attributes=True) for r in rows]

    def user_create(self, data: CreateUserDTO):
        new_user = UserModel(
            email=data.email,
            full_name=data.full_name,
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return UserDTO.model_validate(new_user, from_attributes=True)


def user_create(self, data: CreateUserDTO) -> UserDTO:
    row = UserModel(email=data.email, full_name=data.full_name)
    self.db.add(row)
    self.db.commit()
    self.db.refresh(row)
    return UserDTO.model_validate(row, from_attributes=True)