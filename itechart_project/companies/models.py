from operator import mod
from django.db.models.deletion import CASCADE
from django.db import models

from itechart_project.settings import MEDIA_URL

from .const_values import MaxLenght

# Create your models here.



class TimeCreateUpdate(models.Model): # abstract table
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Employee(TimeCreateUpdate):
    name = models.CharField(max_length=MaxLenght.MAX_EMPLOYEE_NAME_LENGTH)
    surname = models.CharField(max_length=MaxLenght.MAX_EMPLOYEE_SURENAME_LENGTH)
    job_position = models.CharField(max_length=MaxLenght.MAX_EMPLOYEE_JOB_POSITION_LENGTH)
    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    comp_id = models.ForeignKey('Company', on_delete=CASCADE, null=True)
    phone_number = models.PositiveIntegerField(unique=True)
    personal_data_id = models.OneToOneField('PersonalData', on_delete=CASCADE, null=True)


class Bank(TimeCreateUpdate):
    name = models.CharField(max_length=MaxLenght.MAX_BANK_NAME_LENGTH)
    web_site = models.URLField(max_length=MaxLenght.MAX_BANK_WEBSITE_LENGTH)
    email = models.EmailField(max_length=MaxLenght.MAX_BANK_EMAIL_LENGTH, null=True)


class Company(TimeCreateUpdate):
    name = models.CharField(max_length=MaxLenght.MAX_COMPANY_NAME_LENGTH, unique=True)
    web_site = models.URLField(max_length=MaxLenght.MAX_COMPANY_WEBSITE_LENGTH)
    email = models.EmailField(max_length=MaxLenght.MAX_COMPANY_EMAIL_LENGTH, null=True)
    post_index = models.PositiveIntegerField()
    logo = models.ImageField(upload_to=MEDIA_URL, null=True) # settings
    bank = models.ManyToManyField('Bank', null=True)
   

class PersonalData(TimeCreateUpdate):
    date_of_birth = models.DateField()
    home_address = models.CharField(max_length=MaxLenght.MAX_PERSONALDATA_HOMEADRESS_LENGTH)
    salary = models.PositiveIntegerField()
