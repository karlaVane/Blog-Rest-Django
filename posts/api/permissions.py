from rest_framework.permissions import BasePermission

#Solo si es administrador puedes hacer todo, caso contrario, solo pueden leer

class AdminPoderoso(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff