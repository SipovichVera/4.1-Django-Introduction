from django.contrib import admin
from .models import Company, Employee
# Register your models here.
admin.site.register(Employee)
admin.site.register(Company)