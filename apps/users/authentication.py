from rest_framework.authentication import TokenAuthentication


class TokenAuthentication(TokenAuthentication):
    """
    Меняем ключевое слово, которое используется в заголовке Authorization, default = Token
    """

    keyword = "Bearer"
