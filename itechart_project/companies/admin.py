from django.contrib import admin
from .models import Bank, Company, Employee
# Register your models here.
admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(Bank)
