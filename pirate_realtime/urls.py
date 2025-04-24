from django.contrib import admin
from django.urls import path,include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from realtime.views import AreaListCreate, PromotionListCreate
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import TestAuthView

schema_view = get_schema_view(
    openapi.Info(
        title="Pirate Realtime API",
        default_version='v1',
        description="API for real-time promo push with Beacon X Pro W6. WebSocket at /ws/beacon/<user_id>/ sends promo when receiving {'major': int}.",
        contact=openapi.Contact(email="pirate@crew.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/areas/', AreaListCreate.as_view(), name='area-list-create'),
    path('api/promotions/', PromotionListCreate.as_view(), name='promotion-list-create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/test/', TestAuthView.as_view(), name='test_auth'),
    path('api/auth/', include('dj_rest_auth.urls')),  # Login, logout, password reset
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # Signup
    path('accounts/', include('allauth.urls')),  # Social auth, email verification
]