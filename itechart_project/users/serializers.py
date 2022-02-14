from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
import datetime

from .validators import LoginValidator
from .models import User


class RegistrSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = {'username', 'password', 'token'}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)
    last_activity = serializers.DateTimeField(read_only=True)

    def validate(self, data) -> dict:
        username = data.get('username', None)
        password = data.get('password', None)

        login_validator = LoginValidator()
        login_validator.validate_is_blank_field(username, password)

        user = authenticate(username=username, password=password)

        login_validator.validate_user_exists(user)
        login_validator.validate_is_activ(user)
        user.last_activity = datetime.datetime.now()

        return {
            'username': user.username,
            'token': user.token
            }


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username')
