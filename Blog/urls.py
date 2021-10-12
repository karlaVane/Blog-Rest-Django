from django.conf import urls
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from categories.api.router import router_categories
from posts.api.router import router_posts

schema_view = get_schema_view(
   openapi.Info(
      title="BLOG API",
      default_version='v1',
      description="Documentación de la API del Blog",
      terms_of_service="",
      contact=openapi.Contact(email="karla.vanessa@outlook.es"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/',schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui'),
    path('redocs',schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc'),
    path('api/',include('user.api.router')),
    #El ApiViewSet si se importa
    path('api/',include(router_categories.urls)),
    path('api/',include(router_posts.urls))
]
