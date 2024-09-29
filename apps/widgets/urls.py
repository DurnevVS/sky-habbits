from django.urls import path
from . import views

app_name = "widgets"

urlpatterns = [
    path(
        "telegram-widget/",
        views.TelegramWidgetAPIView.as_view(),
        name="telegram-widget",
    ),
    path(
        "telegram-widget-preview/",
        views.telegram_widget_preview,
        name="telegram-widget-preview",
    ),
]
