from rest_framework.test import APITestCase
from lms.models import Course, Lesson
from users.models import User
from rest_framework import status
from django.urls import reverse


class LessonTestCase(APITestCase):

    def setUp(self):
        """Данные для теста(фикстура для теста)."""
        self.user = User.objects.create(email="test@test.com")
        self.course = Course.objects.create(name="Пайтон", description="Курс пайтон")
        self.lesson = Lesson.objects.create(name="Урок пайтон", course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("lms:lessons_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_create(self):
        url = reverse("lms:lessons_create")
        data = {
            "name": "Урок Пайтон 2",
            "course": self.course.pk,
            "video": "https://www.youtube.com",
            "owner": self.user.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("lms:lessons_update", args=(self.lesson.pk,))
        data = {
            "name": "Пайтон нов"
            }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Пайтон нов")

    def test_lesson_delete(self):
        url = reverse("lms:lessons_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)