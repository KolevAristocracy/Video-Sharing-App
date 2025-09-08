import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videoSharing.settings')

app = Celery('videoSharing')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()