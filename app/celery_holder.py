import os

from celery import Celery

redis_server = os.getenv('TASK_QUE_SERVER_REDIS', 'localhost')
redis_url = 'redis://' + redis_server + '/0'

celery = Celery(__name__, broker=redis_url)