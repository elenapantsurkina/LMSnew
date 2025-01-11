from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from .models import Subscription, Course


@shared_task
def send_information_updating_courses(course_id):
    """Отправляет сообщение пользователям об обновлении материалов курса."""
    # Получаем курс по его ID
    course = Course.objects.get(id=course_id)

    # Получаем всех пользователей, подписанных на обновления этого курса
    subscribers = Subscription.objects.filter(course=course).values_list("user__email", flat=True)

    # Формируем сообщение
    subject = "Обновление материалов курса"
    message = f"В материалах курса '{course.name}' произошли обновления."

    # Отправляем письмо каждому подписчику
    for email in subscribers:
        send_mail(subject, message, EMAIL_HOST_USER, [email])
