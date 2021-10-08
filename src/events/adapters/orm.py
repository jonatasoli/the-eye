from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import JSON, DateTime
from sqlalchemy.orm import declarative_base

# declarative base class
Base = declarative_base()

# an example mapping using the base
class Events(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    session_id = Column(String)
    category = Column(String)
    name = Column(String)
    data = Column(JSON)
    timestamp = Column(DateTime)

    def __repr__(self) -> str:
        return f'session: {self.session_id}'

    def to_dict(self) -> dict:
        return dict(
            session_id=self.session_id,
            category=self.category,
            name=self.name,
            data=self.data,
            timestamp=self.timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
        )

