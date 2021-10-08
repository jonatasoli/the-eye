from src.app import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def session_factory(uri=None):
    if not uri:
        with app.app_context():
            uri = app.config.DB_DSN_URI
    return sessionmaker(
        expire_on_commit=False,
        bind=create_engine(
            uri,
        )
    )


