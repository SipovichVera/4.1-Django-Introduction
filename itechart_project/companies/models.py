from operator import mod
from django.db.models.deletion import CASCADE
from django.db import models

# Create your models here.

class TimeCreateUpdate(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


class Employee(TimeCreateUpdate, models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    job_position = models.CharField(max_length=100)
    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    comp = models.ForeignKey('Company', on_delete=CASCADE, null=True)
    phone_number = models.PositiveIntegerField(unique=True)
    personal_data = models.OneToOneField('PersonalData', on_delete=CASCADE)


class Company(TimeCreateUpdate, models.Model):
    name = models.CharField(max_length=100, unique=True)
    web_site = models.URLField(max_length=200)
    email = models.EmailField(max_length=100, null=True)
    post_index = models.PositiveIntegerField()
    logo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    bank = models.ManyToManyField('Bank')


class Bank(TimeCreateUpdate, models.Model):
    name = models.CharField(max_length=100)
    web_site = models.URLField(max_length=200)
    email = models.EmailField(max_length=100, null=True)
   

class PersonalData(TimeCreateUpdate, models.Model):
    date_of_birth = models.DateField()
    home_address = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
