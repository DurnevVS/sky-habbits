from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Habbit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("Пользователь"),
    )
    place = models.TextField(verbose_name=_("Место"))
    action = models.TextField(verbose_name=_("Действие"))
    action_start_time = models.TimeField(verbose_name=_("Время начала действия"))
    action_time_seconds = models.PositiveIntegerField(
        verbose_name=_("Время на выполение действия в секундах")
    )
    period_days = models.PositiveIntegerField(
        verbose_name=_("Периодичность выполнения в днях"),
    )
    is_beneficial = models.BooleanField(
        verbose_name=_("Полезная привычка"),
        default=True,
    )
    reward = models.TextField(
        verbose_name=_("Вознаграждение"),
        blank=True,
        null=True,
    )
    reward_habbit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="related_habbit",
        verbose_name=_("Приятная привычка"),
        blank=True,
        null=True,
    )
    is_public = models.BooleanField(
        verbose_name=_("Публичная привычка"),
        default=False,
    )

    def __str__(self):
        habbit_type = "Полезная" if self.is_beneficial else "Приятная"
        return f"Я буду {self.action} в {self.action_start_time} в {self.place} ({habbit_type} привычка)"
