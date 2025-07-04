from celery import Celery, shared_task
import django
import os 


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_service.settings')

django.setup()

app = Celery("user_service")

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()


@shared_task
def send_welcome_email(email, full_name):

    payload = {
        'to': email,
        'subject': "Welcome to Our Store!",
        'message': f" Hi {full_name} thank you for registering at our site. Hope you'd enjoy this journey with us"
        
    }


