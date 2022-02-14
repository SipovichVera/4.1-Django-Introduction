import datetime
from celery import shared_task
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from django.core.validators import validate_email

from itechart_project.users.models import User


@shared_task
def validate_email_celery(email):
    if validate_email(email) == None:
        return "correct email"


@periodic_task(run_every=(crontab(minute='*/15')))
def remove_inactive_users():
    dt_now = datetime.datetime.now()
    user = (user for user in User.object.all())
    if dt_now - user.last_activity > 365:
        user.is_active = False
