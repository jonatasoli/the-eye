import abc
from src.events.services.unit_of_work import AbstractUnitOfWork
from src.events.domain.model import Event

class AbstractBroker(abc.ABC):

    @abc.abstractmethod
    def pub_event(uow: AbstractUnitOfWork, event: Event):
        raise NotImplementedError

class Broker(AbstractBroker):

    def pub_event(uow, event):
        ...

