import abc
from typing import List
from sqlalchemy import select
from src.events.domain.model import Event


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
        self.session.add(event)

    def list_session(self, session_id):
        smtm = select(Event).where(Event.session_id==session_id)
        return self.session.execute(smtm).all()

    def list_category(self, category):
        smtm = select(Event).where(Event.category==category)
        return self.session.execute(smtm).all()

    def list_timestamp(self, start_date, end_date):
        smtm = select(Event
        ).where(Event.timestamp >= start_date
        ).where(Event.timestamp <=end_date)
        return self.session.execute(smtm).all()
