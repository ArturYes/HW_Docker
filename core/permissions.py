from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsModerator(BasePermission):
    message = "Available only to moderators!"

    def has_permission(self, request, view):
        if request.user.groups.filter(name="moderator").exists():
            return True
        return False


class IsOwner(BasePermission):
    message = "Available only to the owner!"

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
