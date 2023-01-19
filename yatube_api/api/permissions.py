from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.method in SAFE_METHODS
