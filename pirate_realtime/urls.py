from django.contrib import admin
from django.urls import path
from drf_yasg.views import get_swagger_view
from drf_yasg import openapi

swagger = get_swagger_view(title='Pirate Realtime API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', swagger),
]