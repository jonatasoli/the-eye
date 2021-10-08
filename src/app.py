from src.events.factory.app import create_app
from src.events.adapters.celery import init_app


app = create_app()
