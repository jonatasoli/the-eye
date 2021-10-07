from loguru import logger
from .unit_of_work import AbstractUnitOfWork
from src.events.domain.model import Event


class ProcessEvents:
    ...


class ServiceEvents:


    @staticmethod
    def add_event(uow: AbstractUnitOfWork, event: Event):
        with uow:
            _event = uow.events.add(event)
            uow.commit()
            logger.info(f"user create with id {_event.session_id}")


