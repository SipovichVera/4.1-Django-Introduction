from django.urls import path

from .views import Companyview, EmployeeView, bank_view, index

urlpatterns = [path('', index, name="main"),
               path('employee/', EmployeeView.as_view(), name='employee'),
               path('company/', Companyview.as_view(), name='company'),
               path('bank/', bank_view, name='bank'), ]