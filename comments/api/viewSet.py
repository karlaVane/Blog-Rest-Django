from rest_framework.viewsets import ModelViewSet
from comments.models import Comment
from comments.api.serializers import CommentSerializer
from rest_framework.filters import OrderingFilter #Para ordenar los comentarios
from django_filters.rest_framework import DjangoFilterBackend
from comments.api.permissions import IsOwnerOrReadAndCreateOnly

class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]

    #Se puede ver al momento de consultar que se ordena del más antiguo al más reciente
    #Pero quiero que se ordenen del mas actual al más antiguo
    ordering = ['-created_at'] 
    
    ## Para obtener todos los comentarios de un post
    filterset_fields = ['post']

