from rest_framework.serializers import ValidationError


link = "youtube.com"

"""Проверяет на использование ссылки только на yuotube.com."""


def validate_link(value):
    if value not in link:
        raise ValidationError("Ссылка на данный источник не допустима")
