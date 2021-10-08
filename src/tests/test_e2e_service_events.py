import pytest

from src.events.services.unit_of_work import SqlAlchemyUnitOfWork
from src.events.adapters.repository import SqlAlchemyRepository
from src.events.services.service_layer import ServiceEvents
from src.events.adapters import repository, database
from .test_data import session_basic


def test_create_event(postgres_db):
    uow = SqlAlchemyUnitOfWork(
        session_factory=database.session_factory("postgresql://partyoudbuser:partyou123@172.15.0.2/testdb")
    )
    db_event = session_basic
    ServiceEvents.add_event(uow=uow, event=db_event)
    assert uow.events.list_session(
        "e2085be5-9137-4e4e-80b5-f1ffddc25423") is not None

# def test_create_multiple_events():
#     assert uow.commited == True

# def test_search_session_id():
#     assert _session = session_basic

# def test_search_category():
#     assert _session = session_elements

# def test_search_timestamp():
#     assert _session = session_form

# def test_create_event_with_invalid_timestamp():
#     assert exec_info.typename == 'InvalidTimestampException'
