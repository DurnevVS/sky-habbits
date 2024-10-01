import os
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserSerializer


class RegisterUserAPIView(CreateAPIView):
    """
    Регистрация пользователя на сервере для дальнейшей аутентификации по токену.
    Если нужно зарегистрироваться/войти через телеграм использовать /login/telegram/
    """

    serializer_class = UserSerializer
    permission_classes = ()


class LoginTelegramAPIView(APIView):
    """
    Получение ссылки для редиректа на страницу аутентификации по телеграм.
    """

    permission_classes = ()

    @swagger_auto_schema(
        responses={200: '{ "login_url": str }'},
    )
    def get(self, _):
        telegram_request = "https://oauth.telegram.org/auth"
        bot_id = os.environ.get("TELEGRAM_BOT_TOKEN").split(":")[0]
        origin = f'https%3A%2F%2F{os.environ.get("TELEGRAM_BOT_DOMAIN")}'
        embed = 1
        request_access = "write"
        return_to = f"{origin}/widgets/telegram-widget-preview/".replace("/", "%2F").replace(":", "%3A")
        login_url = (
            f"{telegram_request}?"
            f"bot_id={bot_id}&"
            f"origin={origin}&"
            f"embed={embed}&"
            f"request_access={request_access}&"
            f"return_to={return_to}"
        )
        return Response({"login_url": login_url})
