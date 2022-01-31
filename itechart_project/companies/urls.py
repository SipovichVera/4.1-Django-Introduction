from django.urls import path

from .views import Companyview, EmployeeView, LastCreatedEmployee, LastObjInPeriod, SalaryBirthday, bank_view, index

urlpatterns = [path('', index, name="main"),
               path('employee/', EmployeeView.as_view(), name='employee'),
               path('company/', Companyview.as_view(), name='company'),
               path('bank/', bank_view, name='bank'), 
               path('last_date/<slug:date_1>/<slug:date_2>/', LastObjInPeriod.as_view(), name='last_obj_inperiod'),
               path('calary_birthday/<slug:date>/<int:number>/', SalaryBirthday.as_view(), name='calary_birthday'),
            #    path('company_creater/<>')
                path('last_employee/', LastCreatedEmployee.as_view())
               ]