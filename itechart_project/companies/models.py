from mmap import MADV_AUTOSYNC
from operator import mod
from django.db.models.deletion import CASCADE
from django.db import models

# Create your models here.
class MaxLenght():
    MAX_EMPLOYEE_NAME_LENGTH = 100
    MAX_EMPLOYEE_SURENAME_LENGTH = 100
    MAX_EMPLOYEE_JOB_POSITION_LENGTH = 100
    MAX_COMPANY_NAME_LENGTH = 100
    MAX_COMPANY_WEBSITE_LENGTH = 200
    MAX_COMPANY_EMAIL_LENGTH = 100
    MAX_BANK_NAME_LENGTH = 100
    MAX_BANK_WEBSITE_LENGTH = 200
    MAX_BANK_EMAIL_LENGTH = 100
    MAX_PERSONALDATA_HOMEADRESS_LENGTH = 100


class TimeCreateUpdate(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


class Employee(TimeCreateUpdate, models.Model):
    name = models.CharField(max_length=MaxLenght.MAX_EMPLOYEE_NAME_LENGTH)
    surname = models.CharField(max_length=MaxLenght.MAX_EMPLOYEE_SURENAME_LENGTH)
    job_position = models.CharField(max_length=MaxLenght.MAX_EMPLOYEE_JOB_POSITION_LENGTH)
    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    comp = models.ForeignKey('Company', on_delete=CASCADE, null=True)
    phone_number = models.PositiveIntegerField(unique=True)
    personal_data = models.OneToOneField('PersonalData', on_delete=CASCADE)


class Company(TimeCreateUpdate, models.Model):
    name = models.CharField(max_length=MaxLenght.MAX_COMPANY_NAME_LENGTH, unique=True)
    web_site = models.URLField(max_length=MaxLenght.MAX_COMPANY_WEBSITE_LENGTH)
    email = models.EmailField(max_length=MaxLenght.MAX_COMPANY_EMAIL_LENGTH, null=True)
    post_index = models.PositiveIntegerField()
    logo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    bank = models.ManyToManyField('Bank')


class Bank(TimeCreateUpdate, models.Model):
    name = models.CharField(max_length=MaxLenght.MAX_BANK_NAME_LENGTH)
    web_site = models.URLField(max_length=MaxLenght.MAX_BANK_WEBSITE_LENGTH)
    email = models.EmailField(max_length=MaxLenght.MAX_BANK_EMAIL_LENGTH, null=True)
   

class PersonalData(TimeCreateUpdate, models.Model):
    date_of_birth = models.DateField()
    home_address = models.CharField(max_length=MaxLenght.MAX_PERSONALDATA_HOMEADRESS_LENGTH)
    salary = models.PositiveIntegerField()
