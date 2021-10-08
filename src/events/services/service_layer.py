from loguru import logger
from .unit_of_work import AbstractUnitOfWork
from src.events.domain.model import Event
from src.events.adapters.queue import Broker


class ProcessEvents:
    @staticmethod
    def add_event(uow: AbstractUnitOfWork, event: Event):
        with uow:
            uow.events.add(event)
            uow.commit()
            logger.info(f"events create")


class ServiceEvents:

    def enqueue_event(self, event: Event, enqueue: Broker):
        event.check_timestamp()
        enqueue.pub_event(event)
        return dict(message="Event enqueued")





