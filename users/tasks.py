from __future__ import absolute_import, unicode_literals
from celery import shared_task

# from celery.schedules import crontab
# from celery import periodic_task
from django.core.validators import validate_email

from datetime import datetime, timezone
from .models import User


@shared_task
def validate_email_celery(email):
    if validate_email(email) == None:
        return "correct email"


def generate_user():
    for user in User.objects.all():
        yield user
    
@shared_task(name='remove_inactive_users')
# @periodic_task(run_every=(crontab(minute='*/15')))
def remove_inactive_users():
    dt_now = datetime.now(timezone.utc)
    for user in generate_user():
        if dt_now - user.last_activity > 365:
            user.is_active = False
            user.save()
        
