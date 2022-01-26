from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
import jwt


from datetime import datetime, timedelta

from django.conf import settings 
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin
)

from django.db import models

class UserManage(BaseUserManager):

    def create_user(self, username, password=None):
        if username is None:
            raise TypeError("enter login")

        user = self.model(username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password):

        if password is None:
            raise TypeError("enter password")

        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
        username = models.CharField(db_index=True, max_length=255, unique=True)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)
        time_create = models.DateTimeField(auto_now_add=True)
        time_update = models.DateTimeField(auto_now=True)

        USERNAME_FIELD = 'username'
        # REQUIRED_FIELDS = ['username']

        objects = UserManage()

        def __str__(self):
            return self.username

        @property
        def token(self):
            return self._generate_jwt_token()

        def get_full_name(self):
            return self.username

        def get_short_name(self):
            return self.username

        def _generate_jwt_token(self):
            dt = datetime.now() + timedelta(days=1)

            token = jwt.encode({
                'id': self.pk,
                'exp': int(dt.strftime('%s'))
            }, settings.SECRET_KEY, algorithm='HS256')

            return token
