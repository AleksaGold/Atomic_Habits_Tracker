from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):
    """Проверка прав доступа для владельцев."""

    def has_object_permission(self, request, view, obj):
        """Проверяет является ли пользователь владельцем."""
        return obj.owner == request.user


class IsUserPermission(permissions.BasePermission):
    """Проверка прав доступа для пользователя."""

    def has_object_permission(self, request, view, obj):
        """Проверяет является ли пользователь объектом."""
        return obj == request.user
