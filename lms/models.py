from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название курса", help_text="Укажите название курса")
    description = models.TextField(blank=True, null=True, verbose_name="Описание курса", help_text="Укажите описание курса")
    preview = models.ImageField(upload_to="lms/preview/course", blank=True, null=True, verbose_name="Превью", help_text="Загрузите превью")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название урока", help_text="Укажите название урока")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name="Курс", help_text="Выберите курс", blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name="Описание урока", help_text="Укажите описание урока")
    preview = models.ImageField(upload_to="lms/preview/lesson", blank=True, null=True, verbose_name="Превью", help_text="Загрузите превью")
    video = models.CharField(max_length=200, blank=True, null=True, verbose_name="Ссылка на видео", help_text="Укажите ссылку на видео")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name
