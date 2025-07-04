from celery import Celery, shared_task
import django
import os 


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_service.settings')

django.setup()

app = Celery("user_service")

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()



