from django.contrib.auth.models import AbstractUser
from django.db import models


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

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
