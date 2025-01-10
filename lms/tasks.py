
from celery import shared_task
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


@shared_task
def send_information_updating_courses(email):
    """Отправляет сообщение пользователю об обновлении материалов курса."""
    send_mail("Обновление материалов курса",
              "В материалах курсов произошли обновления", EMAIL_HOST_USER, [email])
