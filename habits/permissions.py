from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Права доступа владельца"""

    message = 'Доступ ограничен! Вы не являетесь владельцем записи'

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
