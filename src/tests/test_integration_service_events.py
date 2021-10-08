import pytest

from src.events.domain.model import InvalidTimestampException
from src.events.services.unit_of_work import SqlAlchemyUnitOfWork
from src.events.adapters.repository import SqlAlchemyRepository
from src.events.services.service_layer import ProcessEvents, ServiceEvents
from src.events.adapters import repository, database, queue
from .test_data import session_basic, session_element, session_form,\
    session_invalid_data


class FakeBroker(queue.AbstractBroker):
    def pub_event(uow, event):
        return True


def test_create_event(postgres_db, uow_postgres):
    uow=uow_postgres
    db_event = session_basic
    ProcessEvents.add_event(uow=uow, event=db_event)
    assert uow.events.list_session(
        "e2085be5-9137-4e4e-80b5-f1ffddc25423") is not None

def create_multiple_events(uow_postgres):
    uow=uow_postgres
    event_1 = session_basic
    event_2 = session_element
    event_3 = session_form
    ProcessEvents.add_event(uow=uow, event=event_1)
    ProcessEvents.add_event(uow=uow, event=event_2)
    ProcessEvents.add_event(uow=uow, event=event_3)

# def test_search_session_id():
#     assert _session = session_basic

# def test_search_category():
#     assert _session = session_elements

# def test_search_timestamp():
#     assert _session = session_form

def test_create_event_with_invalid_timestamp():
    event_db = session_invalid_data
    broker = FakeBroker()
    service = ServiceEvents()
    with pytest.raises(InvalidTimestampException) as exc_info:
        service.enqueue_event(event=event_db, enqueue=broker)

    assert exc_info.typename == 'InvalidTimestampException'
