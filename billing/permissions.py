from rest_framework import permissions

class IsAdminIsStaff(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.is_staff:
            return True