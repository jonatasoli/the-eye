from attr import dataclass
from typing import Optional
from datetime import datetime


class InvalidTimestampException(Exception):
    ...


@dataclass
class HostData():
    host: str
    path: str
    element: Optional[str] = None
    form: Optional[dict] = None


class Event():
    def __init__(
        self,
        session_id: str,
        name: str,
        category: str,
        data: HostData,
        timestamp: str,
    ):
        self.session_id = session_id
        self.category = category
        self.name = name
        self.data = data.__dict__
        self.timestamp = datetime.strptime(timestamp, self.get_format_timestamp())

    def check_timestamp(self):
        if self.timestamp >= datetime.now():
            raise InvalidTimestampException()

    @staticmethod
    def get_format_timestamp():
        return "%Y-%m-%d %H:%M:%S.%f"

