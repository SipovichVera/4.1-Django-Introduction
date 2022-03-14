from rest_framework import permissions
from django.core.exceptions import PermissionDenied


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        print(request.user.is_superuser)
        if request.user.is_superuser:
            return True
        else:
            print(request.user)
            raise PermissionDenied("you are not admin")
