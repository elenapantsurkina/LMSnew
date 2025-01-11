from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from lms.models import Course, Lesson


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("У пользователя должна быть почта")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):

    email = models.EmailField(unique=True, verbose_name="Email", help_text="Укажите почту")
    username = None
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Укажите свой номер телефона",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        help_text="Загрузите свой аватар",
    )
    city = models.CharField(
        max_length=35,
        verbose_name="Город",
        blank=True,
        null=True,
        help_text="Укажите свой город",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    # Класс оплат
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    date_of_payment = models.DateField(
        verbose_name="Дата оплаты",
        blank=True,
        null=True,
        help_text="Укажите дату оплаты",
    )
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Оплаченный курс",
        blank=True,
        null=True,
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        verbose_name="Оплаченный урок",
        blank=True,
        null=True,
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
        help_text="Введите сумму оплаты",
        null=True,
        blank=True,
    )
    FORM_PAYMENT_CHOICES = [
        ("transfer_account", "перевод на счет"),
        ("cash", "наличные"),
    ]

    form_of_payment = models.CharField(
        max_length=200,
        verbose_name="Форма оплаты",
        choices=FORM_PAYMENT_CHOICES,
        default="transfer_account",
        help_text="Укажите форму оплаты",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return f"Оплата {self.id} пользователя {self.user.email}" if self.user else "Оплата без пользователя"
