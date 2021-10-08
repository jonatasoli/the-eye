from loguru import logger
from datetime import datetime
from .unit_of_work import AbstractUnitOfWork
from src.events.domain.model import Event
from src.events.adapters.queue import Broker


class ProcessEvents:
    @staticmethod
    def add_event(event: Event, uow: AbstractUnitOfWork):
        with uow:
            uow.events.add(event)
            uow.commit()
            logger.info(f"events create")


class ServiceEvents:

    def enqueue_event(self, event: Event, enqueue: Broker):
        event.check_timestamp()
        enqueue.pub_event(event)
        return dict(message="Event enqueued")

    def search_session(self, session_id: str, uow: AbstractUnitOfWork):
        with uow:
            db_data = uow.events.list_session(session_id)
            events = [row.to_dict() for row in db_data]

        return events

    def search_category(self, category: str, uow: AbstractUnitOfWork):
        with uow:
            db_data = uow.events.list_category(category)
            events = [row.to_dict() for row in db_data]

        return events

    def search_data_range(self, start_date: datetime, end_date: datetime, uow: AbstractUnitOfWork):
        with uow:
            db_data = uow.events.list_timestamp_range(start_date, end_date)
            events = [row.to_dict() for row in db_data]

        return events
