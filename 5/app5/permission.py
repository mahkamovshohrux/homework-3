from rest_framework.permissions import BasePermission

class Staffpermissionclass(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == 2:
            return True

        return False
class Adminpermissionclass(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == 3:
            return True

        return False
