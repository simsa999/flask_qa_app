from db import app
from celery import Celery
from celery.schedules import crontab

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['result_backend'] = 'redis://localhost:6379/0'
app.config['CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP'] = True

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

from CeleryConfig import check_for_new_child_measurement

celery.conf.beat_schedule = {
    'check_for_new_child_measurement': {
        'task': 'CeleryConfig.check_for_new_child_measurement',
        'schedule': crontab(minute=0, hour=8),
    },
}