from app import create_app
from app.celery_instance import configure_celery

# Imported for type hinting
from flask import Flask
from celery import Celery

app: Flask = create_app()
celery: Celery = configure_celery(app)