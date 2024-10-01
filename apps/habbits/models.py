import json
from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver


class Habbit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("Пользователь"),
    )
    name = models.CharField(max_length=255, verbose_name=_("Название"), unique=True)
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
    periodic_task = models.ForeignKey(
        "django_celery_beat.PeriodicTask",
        verbose_name=_("Периодическая задача"),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    def __str__(self):
        habbit_type = "Полезная" if self.is_beneficial else "Приятная"
        return f"Я буду {self.action} в {self.action_start_time} в {self.place} ({habbit_type} привычка)"

    class Meta:
        verbose_name = _("Привычка")
        verbose_name_plural = _("Привычки")


@receiver(pre_save, sender=Habbit)
def create_periodic_task(sender, instance, **kwargs):
    social_accounts = instance.user.social_auth.filter(user=instance.user)
    if social_accounts:
        periodic_task = PeriodicTask.objects.create(
            name=instance.user.username + instance.name,
            task="apps.habbits.tasks.telegram_remaind",
            interval=IntervalSchedule.objects.get(every=instance.period_days),
            start_time=datetime.combine(
                date=datetime.today().date(),
                time=instance.action_start_time,
            ),
            kwargs=json.dumps(
                {
                    "telegram_uid": social_accounts.get(provider="telegram").uid,
                    "user_id": instance.user.id,
                    "habbit_name": instance.name,
                }
            ),
        )
        instance.periodic_task = periodic_task


@receiver(pre_delete, sender=Habbit)
def delete_periodic_task(sender, instance, **kwargs):
    if instance.periodic_task:
        instance.periodic_task.delete()
