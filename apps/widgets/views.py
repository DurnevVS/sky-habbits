from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class TelegramWidgetAPIView(APIView):
    def get(self, request):
        return Response(
            {
                "widget": "telegram-widget",
            }
        )


def telegram_widget_preview(request):
    return render(request, "widgets/telegram-widget-preview.html")
