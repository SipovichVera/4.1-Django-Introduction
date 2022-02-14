import email
from django.http import HttpResponse
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.csrf import csrf_exempt

from .tasks import validate_email_celery
from .permissions import IsAdmin
from .serializers import LoginSerializer, RegistrSerializer, UserSerializer


class RegistrAPIView(APIView):
    permission_classes = (IsAdmin,)
    serializer_class = RegistrSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.data)
        return Response(serializer.data)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

@csrf_exempt
def check_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        return HttpResponse(validate_email_celery.delay(email))  # delay() - Celery to execute this function in the background
    return HttpResponse("enter email")