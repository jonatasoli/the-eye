#!/bin/sh

# Start Celery
celery -A src.celery_worker.celery_obj worker --loglevel=info --pidfile=celery@%h.pid --logfile=logs/celery_worker001@%h.log --detach -n worker001@%h
