import eventlet
eventlet.monkey_patch()

import datetime
from celery import shared_task
from django.utils import timezone
from users.models import User


@shared_task
def checking_for_active_users():
    """Проверяет заходил ли пользователь более 30 дн и блокирует если не заходил."""
    thirty_days_ago = timezone.now() - datetime.timedelta(days=30)
    users = User.objects.filter(last_login__lt=thirty_days_ago).exclude(last_login__isnull=True)
    users.update(is_active=False)
    users.save()
