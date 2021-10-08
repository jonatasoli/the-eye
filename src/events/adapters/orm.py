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
