#!/usr/bin/env python
import os
from src.app import app
from src.events.adapters.celery import celery_obj

app.app_context().push()
