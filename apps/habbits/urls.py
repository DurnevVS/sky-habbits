from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "habbits"
router = DefaultRouter()
router.register("", views.HabbitsViewSet, "habbits")


urlpatterns = [
    path("", include(router.urls)),
    path("public/", views.PublicHabbitsListAPIView.as_view(), name="public"),
]
