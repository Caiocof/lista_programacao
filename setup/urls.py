from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from aluraflix.views import ProgramaViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Aluraflix",
        default_version='v1',
        description="Criar um sistema de series e filmes",
        terms_of_service="#",
        contact=openapi.Contact(email="caiooliveira3652@outlook.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('programas', ProgramaViewSet, basename='programas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
