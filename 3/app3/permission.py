from rest_framework.permissions import BasePermission


class StaffPermission3(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == 2:
            return True
        return False
class AdminPrmission3(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == 3:
            return True
        return False