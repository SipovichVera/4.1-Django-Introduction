from http.client import HTTPResponse
from django.http import HttpResponse
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.db.models import Q

from .models import Bank, Company, Employee
from .serializers import BankSerializer, CompanySerializer, EmployeeSerializer

# Create your views here.
def index(request):
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
        print(request)
        queryset = self.get_queryset()
        serializer = CompanySerializer(queryset, many=True)
        return HttpResponse(serializer.data)

    def create(self, request):
    #     print(request.data)
    #     Company.objects.create(**request.data)
    #     return HttpResponse(request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.data)
        return HttpResponse(serializer.data)



# banks (Function Based Views)
@csrf_exempt
@permission_classes([AllowAny])
def bank_view(request):
    if request.method == 'GET':
        bank_objects = Bank.objects.all()
        return HttpResponse(bank_objects)

    if request.method == 'POST':
        serializer = BankSerializer(data=dict(request.POST.items()))
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.data)
        return HttpResponse(serializer.data)

        
class LastObjInPeriod(APIView):

    def get(self, request, date_1, date_2):
        return HttpResponse(Company.objects.filter(Q(time_create__lt=date_2)&
               Q(time_create__gt=date_1)).latest('time_create'))
