from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .swagger import OpenAPISchemaGenerator

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    generator_class=OpenAPISchemaGenerator,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    re_path(r"^auth/", include("drf_social_oauth2.urls", namespace="drf")),
    re_path(r"^social/", include("social_django.urls", namespace="social")),
    path("widgets/", include("apps.widgets.urls", namespace="widgets")),
    path("users/", include("apps.users.urls", namespace="users")),
    path("habbits/", include("apps.habbits.urls", namespace="habbits")),
]
