from rest_framework import permissions


class UserViewSetPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'create':
            return not request.user.is_authenticated
        elif view.action == 'list':
            return False
        else:
            return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ['retrieve', 'me', 'partial_update', 'destroy']:
            return obj == request.user or request.user.is_staff
        else:
            return False
