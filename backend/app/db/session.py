from typing import Generator
from sqlalchemy.orm import Session
from .base import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 