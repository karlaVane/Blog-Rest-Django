from rest_framework.viewsets import ModelViewSet
from posts.models import Posts
from posts.api.serializers import PostSerializer
from posts.api.permissions import AdminPoderoso
from django_filters.rest_framework import DjangoFilterBackend

class PostApiViewSet(ModelViewSet):
    permission_classes = [AdminPoderoso]
    serializer_class = PostSerializer
    queryset = Posts.objects.filter(published=True)
    #lookup_field = 'slug' #En lugar de hacer la búsqueda por el id se hará por el slug
    filter_backends = [DjangoFilterBackend]

    #Opción para poder filtrar con más de dos campos
    filterset_fields = ['category','category__title'] #filtrar por el titulo de la categoría. Buscar así para el url
    # filterset_fields = ['category']