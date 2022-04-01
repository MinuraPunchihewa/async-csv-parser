from celery import Celery
from flask import Flask

from app import celery_holder


def configure_celery(app: Flask) -> Celery:
    TaskBase = celery_holder.celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery_holder.celery.conf.update(app.config)
    celery_holder.celery.Task = ContextTask

    return celery_holder.celery
