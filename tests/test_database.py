from sqlalchemy import text

from app.database.connection import (
    DATABASE_URL,
    SessionLocal,
)


def test_database_url_exists():
    assert DATABASE_URL is not None
    assert DATABASE_URL


def test_database_connection():
    db = SessionLocal()

    try:
        result = db.execute(text("SELECT 1"))

        assert result.scalar() == 1

    finally:
        db.close()
