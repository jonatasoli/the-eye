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


from src.app import app
from src.events.adapters.orm import Base
from src import create_app

pytest.register_assert_rewrite("tests.e2e.api_client")


# @pytest.fixture(scope="session", autouse=True)
# def set_test_settings():
#     app.config.FORCE_ENV_FOR_DYNACONF="testing"

@pytest.fixture(scope="module")
def test_app():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    # app.config.from_object("src.config.TestingConfig")
    with app.app_context():
        yield app  # testing happens here


@pytest.fixture
def postgres_db():
    engine = create_engine("postgresql://partyoudbuser:partyou123@172.15.0.2/testdb")
    with engine.begin() as conn:
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
