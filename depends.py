from typing import Any, Generator

from app.database.db_connection import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends

def get_db() -> Generator[Any, Any, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()