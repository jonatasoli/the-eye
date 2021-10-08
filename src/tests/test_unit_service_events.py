import pytest

from src.events.services.unit_of_work import AbstractUnitOfWork
from src.events.adapters.repository import AbstractRepository
from src.events.services.service_layer import ServiceEvents, ProcessEvents
from src.events.adapters import queue
from .test_data import session_basic


class FakeRepository(AbstractRepository):
    def __init__(self, event):
        self._event = set(event)

    def add(self, event):
        self._event.add(event)
        return event

    def list_session(self, session_id):
        list = [b for b in self._event if b.session_id == session_id]
        return list

    def list_category(self, category):
        return list(self._event)

    def list_timestamp_range(self, end_date, start_date):
        return list(self._event)


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.events = FakeRepository([])
        self.committed = False

    def _commit(self):
        self.committed = True

    def rollback(self):
        pass


class FakeBroker(queue.AbstractBroker):
    def pub_event(uow, event):
        return True


def test_create_event():
    uow = FakeUnitOfWork()
    db_event = session_basic
    ProcessEvents.add_event(uow=uow, event=db_event)
    assert uow.events.list_session(
        "e2085be5-9137-4e4e-80b5-f1ffddc25423") is not None
    assert uow.committed


def test_queue_event():
    broker = FakeBroker()
    db_event = session_basic
    service = ServiceEvents()
    output = service.enqueue_event(event=db_event, enqueue=broker)
    assert output == dict(message="Event enqueued")

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
