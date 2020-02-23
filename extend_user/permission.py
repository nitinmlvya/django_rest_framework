from rest_framework.permissions import BasePermission


class IsUserOnly(BasePermission):
    def has_permission(self, request, view):
        print('User: ', request.user)
        if request.user.role.name == 'admin':
            return True
        else:
            return False
