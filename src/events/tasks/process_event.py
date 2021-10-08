from loguru import logger
from src.events.adapters.celery import celery_obj as celery
from src.events.domain.model import Event
from src.events.services import service_layer, unit_of_work

@celery.task(
    name='events_queue',
    bind=True,
    default_retry_delay=5,
    max_retries=10)
def background_event_process(
    event: Event,
    uow: unit_of_work.AbstractUnitOfWork = unit_of_work.SqlAlchemyUnitOfWork
    ):

    try:
        service =service_layer.ProcessEvents()
        service.add_event(event=event, uow=uow)
        logger.info("Event is process")
    except Exception as e:
        raise e
