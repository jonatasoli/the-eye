from loguru import logger
from src.events.adapters.celery import celery_obj as celery
from src.events.domain.model import Event, HostData
from src.events.services import service_layer, unit_of_work

@celery.task(
    name='events_queue',
    bind=True,
    default_retry_delay=5,
    max_retries=10)
def background_event_process(
    self,
    event,
    uow: unit_of_work.AbstractUnitOfWork = unit_of_work.SqlAlchemyUnitOfWork()
    ):

    try:
        logger.info("start task")
        _data = event.get('data')
        _event = Event(
            session_id = event.get('session_id'),
            category = event.get('category'),
            name = event.get('name'),
            data = HostData(
                host=_data.get('host'),
                path=_data.get('path'),
                element=_data.get('element'),
                form=_data.get('form'),
            ),
            timestamp = event.get('timestamp')
        )
        service =service_layer.ProcessEvents()
        service.add_event(event=_event, uow=uow)
        logger.info("Event is process")
    except Exception as e:
        raise e
