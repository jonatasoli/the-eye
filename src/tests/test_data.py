from src.events.domain.model import Event, HostData
from datetime import datetime, timedelta


today = datetime.now()
tomorrow = today + timedelta(days=1)


session_basic = Event(
    session_id="e2085be5-9137-4e4e-80b5-f1ffddc25423",
    category="page interaction",
    name="pageview",
    data=HostData(
        host="www.consumeraffairs.com",
        path="/",
    ),
    timestamp="2021-01-01 09:15:27.243860"
)

session_element = Event(
  session_id="e2085be5-9137-4e4e-80b5-f1ffddc25423",
  category="page interaction",
  name="cta click",
  data=HostData(
    host="www.consumeraffairs.com",
    path="/",
    element="chat bubble"
  ),
  timestamp="2021-01-01 09:15:27.243860"
)

session_form = Event(
  session_id="e2085be5-9137-4e4e-80b5-f1ffddc25423",
  category="form interaction",
  name="submit",
  data=HostData(
    host="www.consumeraffairs.com",
    path="/",
    form=dict(
      first_name="John",
      last_name="Doe"
    )
  ),
  timestamp="2021-01-01 09:15:27.243860"
)


session_invalid_data = Event(
  session_id="e2085be5-9137-4e4e-80b5-f1ffddc25423",
  category="form interaction",
  name="submit",
  data=HostData(
    host="www.consumeraffairs.com",
    path="/",
    form=dict(
      first_name="John",
      last_name="Doe"
    )
  ),
  timestamp=tomorrow.strftime("%Y-%m-%d %H:%M:%S.%f")
)
