from celery import Celery, shared_task


@shared_task
def authenticate_user(token):

    print(token)

    return token


