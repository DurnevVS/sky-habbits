from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = "users"


urlpatterns = [
    path("register/", views.RegisterUserAPIView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="login"),
    path(
        "login/telegram/", views.LoginTelegramAPIView.as_view(), name="login-telegram"
    ),
]
