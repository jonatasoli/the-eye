from src.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def session_factory():
    if not hasattr(settings, "DB_DSN_URI"):
        return None
    return sessionmaker(
        expire_on_commit=False,
        bind=create_engine(
            settings.DB_DSN_URI,
        )
    )


