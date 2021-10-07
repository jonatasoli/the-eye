from attr import dataclass
from typing import Optional
from datetime import datetime


class InvalidTimestampException(Exception):
    ...


@dataclass
class FormData():
    first_name: str
    last_name: str


@dataclass
class HostData():
    host: str
    path: str
    element: Optional[str] = None
    form: Optional[FormData] = None


class Event():
    def __init__(
        self,
        session_id,
        name,
        category,
        data,
        timestamp,
    ):
        self.format = "%Y-%m-%d %H:%M:%S.%f"
        self.session_id = session_id
        self.category = category
        self.name = name
        self.data = data
        self.timestamp = datetime.strptime(timestamp, self.format)

    def check_timestamp(self):
        if self.timestamp >= datetime.now():
            raise InvalidTimestampException()
