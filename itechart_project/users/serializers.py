from dataclasses import field
from rest_framework import serializers
from django.contrib.auth import authenticate

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

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError(
                'username is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'password is required to log in.'
            )

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                "no such user"
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user is deactivated.'
            )

        return {
            'username': user.username,
            'token': user.token
            }