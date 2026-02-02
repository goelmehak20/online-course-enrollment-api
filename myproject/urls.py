from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from django.shortcuts import redirect

def home(request):
    return redirect("/api/schema/swagger-ui/")

def api_fallback(request):
    return redirect("/api/")

urlpatterns = [
    path("", home),
    path("api/", api_fallback),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # ✅ CORRECT drf-spectacular URLs
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    path("silk/", include("silk.urls", namespace="silk")),
]
