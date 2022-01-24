from http.client import HTTPResponse
from django.http import HttpResponse
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from httplib2 import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics

from .models import Bank, Company, Employee
from .serializers import BankSerializer, CompanySerializer, EmployeeSerializer
from . import serializers

# Create your views here.
def main_page(request):
    return HTTPResponse('<h1>hello</h1>')


# employees (Class Based Views)
class EmployeeView(APIView):
    permission_classes = [AllowAny]
    serializer_class = EmployeeSerializer
    objects = Employee.objects.all()


    def get(self, request):
        return HttpResponse(self.objects)

    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.data)
        return HttpResponse(serializer.data)


# companies (Generic Views)
class Companyview(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [AllowAny] 

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        print(request.data)
        Company.objects.create(**request.data)
        return HttpResponse(request.data)
        # serializer = self.serializer_class(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.create(serializer.data)
        # return HttpResponse(serializer.data)



# banks (Function Based Views)
@permission_classes([AllowAny])
def bank_view(request):
    if request.method == 'GET':
        bank_objects = Bank.objects.all()
        return HttpResponse(bank_objects)

    if request.method == 'POST':
        print(request.data)
        serializer = BankSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.data)
        return HttpResponse(serializer.data)

        

