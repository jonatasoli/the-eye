# pylint: disable=redefined-outer-name
import shutil
import subprocess
import time
from pathlib import Path

import pytest
import httpx
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers


from src.events.factory.app import create_app
from src.events.adapters.orm import Base
from src.events.adapters import database
from src.events.services.unit_of_work import SqlAlchemyUnitOfWork


@pytest.fixture(scope="module")
def test_app():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    with app.app_context():
        yield app  # testing happens here


@pytest.fixture
def postgres_db():
    engine = create_engine("postgresql://myuser:mypass@172.18.0.3/testdb")
    with engine.begin() as conn:
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)

@pytest.fixture
def uow_postgres():
    return SqlAlchemyUnitOfWork(
        session_factory=database.session_factory(
            "postgresql://myuser:mypass@172.18.0.3/testdb"
        )
    )

