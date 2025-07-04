from celery import shared_task
import time

@shared_task
def send_email_task(to_email):
    print(f"Sending email to {to_email} ...")
    time.sleep(2)
    print(f"Email sent to {to_email}!")
    return True




@shared_task
def send_welcome_email(email, full_name):

    payload = {
        'to': email,
        'subject': "Welcome to Our Store!",
        'message': f" Hi {full_name} thank you for registering at our site. Hope you'd enjoy this journey with us"
        
    }

    print(payload)
