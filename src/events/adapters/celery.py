import celery
from loguru import logger
from flask import Flask

celery_obj = celery.Celery(__name__)


def init_app(app: Flask):
    logger.info(app.config['CELERY_BROKER_URL'])
    logger.info(app.config['CELERY_RESULT_BACKEND'])
    celery_obj.conf.broker_url = app.config['CELERY_BROKER_URL']
    celery_obj.conf.result_backend = app.config['CELERY_RESULT_BACKEND']

    TaskBase = celery_obj.Task

    class AppContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = AppContextTask
