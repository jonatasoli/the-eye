import pytest
from .test_data import session_basic, session_invalid_data
from src.events.domain.model import InvalidTimestampException

def test_valid_data():
    assert session_basic.check_timestamp() is None


def test_invalid_data():
    with pytest.raises(InvalidTimestampException) as exc_info:
        session_invalid_data.check_timestamp()
    assert exc_info.typename == 'InvalidTimestampException'
