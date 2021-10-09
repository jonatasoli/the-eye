import abc
from typing import List
from sqlalchemy import select, between
from src.events.domain.model import Event
from .orm import Events


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, event: Event):
        raise NotImplementedError

    @abc.abstractmethod
    def list_session(self, session_id) -> List[Event]:
        raise NotImplementedError

    @abc.abstractmethod
    def list_category(self, category) -> List[Event]:
        raise NotImplementedError

    @abc.abstractmethod
    def list_timestamp_range(self, start_date, end_date) -> List[Event]:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, event):
        self.session.add(
            Events(
                session_id = event.session_id,
                category = event.category,
                name = event.name,
                data = event.data,
                timestamp = event.timestamp
            )
        )

    def list_session(self, session_id):
        smtm = select(Events).where(Events.session_id==session_id)
        return self.session.execute(smtm).scalars().all()

    def list_category(self, category):
        smtm = select(Events).where(Events.category==category)
        return self.session.execute(smtm).scalars().all()

    def list_timestamp_range(self, start_date, end_date):
        smtm = select(Events
        ).where(between(Events.timestamp, start_date,end_date))
        return self.session.execute(smtm).scalars().all()
