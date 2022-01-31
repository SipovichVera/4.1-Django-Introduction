from django.contrib import admin
from .models import Bank, Company, Employee, PersonalData
# Register your models here.
admin.site.register(Employee)
admin.site.register(Company)
admin.site.register(Bank)
admin.site.register(PersonalData)
