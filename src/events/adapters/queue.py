import abc
from loguru import logger

from src.events.services.unit_of_work import AbstractUnitOfWork
from src.events.domain.model import Event
from src.events.tasks import process_event

class AbstractBroker(abc.ABC):

    @abc.abstractmethod
    def pub_event(uow: AbstractUnitOfWork, event: Event):
        raise NotImplementedError

class Broker(AbstractBroker):

    def pub_event(self, event):
        try:
            process_event.background_event_process.delay(event=event)
            logger.info("Pub message in a broker")
        except Exception as e:
            raise e

