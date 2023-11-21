from RoutesInterfaceIn import *
from celery import Celery

celery = Celery(
    'your_flask_app',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)
