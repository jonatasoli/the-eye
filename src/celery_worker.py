#!/usr/bin/env python
import os
from src.app import app
from src.events.adapters.celery import celery_obj
from src.events.tasks import process_event

app.app_context().push()
