from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = "habbits"
router = DefaultRouter()
router.register("private", views.HabbitsViewSet, "habbits")


urlpatterns = [
    path("public/", views.PublicHabbitsListAPIView.as_view(), name="public"),
]
urlpatterns += router.urls
