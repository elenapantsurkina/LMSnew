from django.db import models
from django.conf import settings


class Course(models.Model):
    """Модель курс."""
    name = models.CharField(
        max_length=50,
        verbose_name="Название курса",
        help_text="Укажите название курса")
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание курса",
        help_text="Укажите описание курса")
    preview = models.ImageField(
        upload_to="lms/preview/course",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """Модель урок."""
    name = models.CharField(
        max_length=50,
        verbose_name="Название урока",
        help_text="Укажите название урока")
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        help_text="Выберите курс",
        blank=True,
        null=True)
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание урока",
        help_text="Укажите описание урока")
    preview = models.ImageField(
        upload_to="lms/preview/lesson",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью")
    video = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name


class Subscription(models.Model):
    """Подписка на обновления курса для пользователя."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Владелец",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс")

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"


class CoursePayment(models.Model):
    """Модель оплаты курсов"""
    amount = models.PositiveIntegerField(
        verbose_name="Оплата за курс",
        help_text="Укажите сумму оплаты",
    )
    session_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Id сессии",
        help_text="Укажите Id сессии"
    )
    link = models.URLField(
        max_length=400,
        blank=True,
        null=True,
        verbose_name="Ссылка на оплату",
        help_text="Укажите ссылку на оплату"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Владелец",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Оплата курса"
        verbose_name_plural = "Оплата курсов"

    def __str__(self):
        return self.amount
