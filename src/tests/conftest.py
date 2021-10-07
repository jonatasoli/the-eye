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
from tenacity import retry, stop_after_delay


from src.config import settings

from src import create_app

pytest.register_assert_rewrite("tests.e2e.api_client")


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    # app.config.from_object("src.config.TestingConfig")
    with app.app_context():
        yield app  # testing happens here
