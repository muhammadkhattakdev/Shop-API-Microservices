from celery import shared_task
import time

@shared_task
def send_email_task(to_email):
    print(f"Sending email to {to_email} ...")
    time.sleep(2)
    print(f"Email sent to {to_email}!")
    return True




