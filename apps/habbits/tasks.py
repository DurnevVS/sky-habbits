from celery import shared_task
import requests
import os
from .models import Habbit


@shared_task
def telegram_remaind(*, telegram_uid, user_id, habbit_name):
    habbit = Habbit.objects.get(user__id=user_id, name=habbit_name)
    requests.get(
        f"https://api.telegram.org/bot{os.environ.get('TELEGRAM_BOT_TOKEN')}/"
        f"sendMessage?"
        f"chat_id={telegram_uid}&"
        f"text={habbit}"
    )
