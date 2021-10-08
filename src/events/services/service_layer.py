from loguru import logger
from .unit_of_work import AbstractUnitOfWork
from src.events.domain.model import Event


class ProcessEvents:
    ...


class ServiceEvents:


    @staticmethod
    def add_event(uow: AbstractUnitOfWork, event: Event):
        with uow:
            import ipdb; ipdb.set_trace()
            uow.events.add(event)
            uow.commit()
            logger.info(f"events create")


