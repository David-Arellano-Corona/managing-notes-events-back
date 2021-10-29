from rest_framework import permissions
from .exceptions import Forbidden

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if(obj.owner != request.user):
            raise Forbidden()
        return True