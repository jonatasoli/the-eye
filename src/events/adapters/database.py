from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def session_factory(uri=None):
    if not uri:
        uri = config('SQLALCHEMY_DATABASE_URI')
    return sessionmaker(
        expire_on_commit=False,
        bind=create_engine(
            uri,
        )
    )


