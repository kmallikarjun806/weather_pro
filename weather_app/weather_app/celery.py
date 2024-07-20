from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_app.settings')

app = Celery('weather_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update-weather-data-every-10-minutes': {
        'task': 'weather.tasks.update_weather_data',
        'schedule': crontab(minute='*/10'),
    },
}
