from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        """Чтение все. Измнения только авторизованные пользователи"""
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """Чтение все. Изменения только авторы."""
        print('\n\nview:', view)
        print('dir(view):', view.detail)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsOwnerOrReadOnlyToComments(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class OwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
