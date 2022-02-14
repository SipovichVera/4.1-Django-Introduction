import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "itechart_project.settings")
app = Celery("itechart_project")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()