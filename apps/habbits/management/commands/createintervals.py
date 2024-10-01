from django.core.management.base import BaseCommand
from django_celery_beat.models import IntervalSchedule


class Command(BaseCommand):
    """
    Создает интервалы "каждые 1 - 7 дней" для использования в привычках
    """

    def handle(self, *args, **options):
        [
            IntervalSchedule.objects.create(id=i, every=i, period="days")
            for i in range(1, 8)
        ]

    print("Интервалы созданы")
