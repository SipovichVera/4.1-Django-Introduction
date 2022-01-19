from operator import mod
from django.db.models.deletion import PROTECT, CASCADE
from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    job_position = models.CharField(max_length=100)
    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    company = models.ForeignKey('Company', on_delete=CASCADE, null=True)
    phone_number = models.PositiveIntegerField(max_length=9, unique=True)
    personal_data = models.OneToOneField('PersonalData', on_delete=CASCADE)

