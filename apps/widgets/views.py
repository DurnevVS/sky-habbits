from django.shortcuts import render
from django.template.loader import render_to_string
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .serializers import TelegramWidgetSerializer


class TelegramWidgetAPIView(APIView):
    """
    Получения source-code виджета телеграмма с настройками,
    который можно использовать для использования на своём сайте.
    Можно выбрать размер кнопки и радиус закругления углов.
    """

    @swagger_auto_schema(
        query_serializer=TelegramWidgetSerializer,
        responses={200: '{ "preview_url": str, source_code": str }'},
    )
    def get(self, request: Request):
        serializer = TelegramWidgetSerializer(data=request.query_params)
        if serializer.is_valid():
            size = serializer.validated_data["size"]
            radius = serializer.validated_data["radius"]
            preview_url = request.build_absolute_uri(
                f"/widgets/telegram-widget-preview/?size={size}&radius={radius}"
            )
            source_code = render_to_string(
                "widgets/telegram-widget.html", {"size": size, "radius": radius}
            )
            return Response({"preview_url": preview_url, "source_code": source_code})
        return Response(serializer.errors)


def telegram_widget_preview(request):
    size = request.GET.get("size")
    radius = request.GET.get("radius")
    return render(
        request,
        "widgets/telegram-widget-preview.html",
        {
            "size": size,
            "radius": radius,
        },
    )
