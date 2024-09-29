from django.urls import path
from . import views

app_name = "habbits"

urlpatterns = [
    path("", views.HabbitsListAPIView.as_view(), name="habbits_list"),
]
