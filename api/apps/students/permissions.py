from rest_framework import permissions


class IsOwnerOfStudent(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
