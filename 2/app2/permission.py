from rest_framework.permissions import BasePermission


class Adminpermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == 3:
            return True
        
        return False
    
class Staffpermissin(BasePermission):
    def has_permission(self, request, view):
        if request.user.roles == 2:
            return True
        return False