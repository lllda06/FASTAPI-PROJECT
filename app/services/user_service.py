from sqlalchemy.orm import Session
from app.dto.user_dto import CreateUserDTO, UserDTO
from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    @classmethod
    def from_session(cls, db: Session) -> "UserService":
        return cls(UserRepository(db))

    def list_users(self, skip: int = 0, limit: int = 100) -> list[UserDTO]:
        return self.repo.users_list(skip, limit)

    def get_user(self, user_id: int) -> UserDTO:
        return self.repo.user_get(user_id)

    def create_user(self, param: CreateUserDTO) -> UserDTO:
        user = self.repo.user_create(param)
        return user