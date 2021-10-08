import pytest
from datetime import datetime

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

def create_multiple_events(uow):
    event_1 = session_basic
    event_2 = session_element
    event_3 = session_form
    ProcessEvents.add_event(uow=uow, event=event_1)
    ProcessEvents.add_event(uow=uow, event=event_2)
    ProcessEvents.add_event(uow=uow, event=event_3)

def test_search_session_id(uow_postgres):
    create_multiple_events(uow=uow_postgres)
    _service_id="e2085be5-9137-4e4e-80b5-f1ffddc25423"
    service = ServiceEvents()
    _session = service.search_session(session_id=_service_id, uow=uow_postgres)
    assert len(_session) == 4

def test_search_category(uow_postgres):
    _category="form interaction"
    service = ServiceEvents()
    _session = service.search_category(category=_category, uow=uow_postgres)
    assert _session[0] == session_form.to_json()

def test_search_timestamp(uow_postgres):
    _start_date = datetime(2021,1,1,9,25,00)
    _end_date = datetime(2021,1,1,9,26,00)
    service = ServiceEvents()
    _session = service.search_data_range(
        start_date=_start_date,
        end_date=_end_date,
        uow=uow_postgres
    )
    assert _session[0] == session_element.to_json()

def test_create_event_with_invalid_timestamp():
    event_db = session_invalid_data
    broker = FakeBroker()
    service = ServiceEvents()
    with pytest.raises(InvalidTimestampException) as exc_info:
        service.enqueue_event(event=event_db, enqueue=broker)

    assert exc_info.typename == 'InvalidTimestampException'


def test_pub_celery():
    event = session_basic
    broker = queue.Broker()
    service = ServiceEvents()
    output = service.enqueue_event(event=event, enqueue=broker)
    assert output == dict(message="Event enqueued")

