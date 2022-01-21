from http.client import HTTPResponse
from rest_framework.decorators import permission_classes
from django.views import APIView
from httplib2 import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics

from itechart_project.companies.models import Bank, Company, Employee
from itechart_project.companies.serializers import BankSerializer, CompanySerializer, EmployeeSerializer

# Create your views here.
def main_page(request):
    return HTTPResponse('<h1>hello</h1>')

def get_employee_objects():
    return Employee.objects.all()

# employees (Class Based Views)
class EmployeeView(APIView):
    # permission_classes = [AllowAny]

    def get(self, request):
        return Response(get_employee_objects())

    def post(self, request):
        serializer = EmployeeSerializer(request.data)


# companies (Generic Views)
class Companyview(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_classes = CompanySerializer
    permission_classes = [AllowAny] 

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)

# banks (Function Based Views)
@permission_classes([AllowAny])
def bank_view(request):
    if request.method == 'GET':
        bank_objects = Bank.objects.all()
        return Response(bank_objects)

    if request.method == 'POST':
        serializer = BankSerializer(request.data)
        

