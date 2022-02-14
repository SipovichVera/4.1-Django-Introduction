from celery import shared_task
from django.core.validators import validate_email


@shared_task
def validate_email_celery(email):
    if validate_email(email) == None:
        return "correct email"