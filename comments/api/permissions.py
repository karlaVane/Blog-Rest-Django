# Todo el mundo va a poder leer y crear 
# Pero solo el propietario del post podrá modifica y eliminar

from rest_framework.permissions import BasePermission
from comments.models import Comment

class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            id_comment = view.kwargs['pk'] #Se obtiene solo el id del comentario
            comment = Comment.objects.get(pk = id_comment) #trae el comentario de la bd

            id_user = request.user.pk #id del usuario q esta ejecutando la petición
            id_user_comment = comment.user_id #id del comentario que hemos obtenido 

            if id_user == id_user_comment: #comparación de id
                return True
            
            return False