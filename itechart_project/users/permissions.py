from django.http import Http404
from rest_framework import permissions

class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            print(request.user)
            raise Http404("you are not admin")