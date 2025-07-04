import os
from celery import Celery, shared_task
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_service.settings')

django.setup()

app = Celery('email_service')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()





