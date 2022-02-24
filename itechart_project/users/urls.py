
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import LoginAPIView, RegistrAPIView, UserAPIView, check_email, get_all_users

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('', UserAPIView.as_view(), name='user'),
    path('registr', UserAPIView.as_view(), name='registr'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('email/', check_email),
    path('all_users/', get_all_users),
]
