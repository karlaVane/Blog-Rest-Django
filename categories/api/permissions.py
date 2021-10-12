from rest_framework.permissions import BasePermission

#Solo si es administrador puede hacer todo caso contrario solo puede leer
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff
        