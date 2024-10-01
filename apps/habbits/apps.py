from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HabbitsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.habbits"
    verbose_name = _("Привычки")
