from django.core.management.base import BaseCommand
from lms.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    help = 'Add test data to the database'

    def handle(self, *args, **options):
        #  Создаем курсы
        course1 = Course.objects.create(
            name="Джанго",
            description="Добрый добрый джанго",
            preview=None
        )

        course2 = Course.objects.create(
            name="Пайтон",
            description="Пайтон великолепный",
            preview=None
        )

        self.stdout.write(self.style.SUCCESS("Курсы созданы успешно."))

        # Создаем уроки
        lesson1 = Lesson.objects.create(
            name="Джанго1",
            course=course1,
            description="Джанго начало",
            preview=None,
            video=None
        )

        lesson2 = Lesson.objects.create(
            name="Джанго2",
            course=course1,
            description="Джанго продвинутый",
            preview=None,
            video=None
        )

        lesson3 = Lesson.objects.create(
            name="Пайтон1",
            course=course2,
            description="Пайтон начало",
            preview=None,
            video=None
        )

        self.stdout.write(self.style.SUCCESS("Уроки созданы успешно."))

        # Создаем пользователя
        params = dict(email="sky@example.com", password="bnmqwe45")
        user, created = User.objects.get_or_create(params)
        user.is_staff = True
        user.save()

        self.stdout.write(self.style.SUCCESS("Пользователь создан успешно."))

        # Создаем платежи
        Payment.objects.create(
            user=user,
            date_of_payment="2023-12-12",
            paid_course=course1,
            paid_lesson=None,
            amount=2000.00,
            form_of_payment="transfer_account",
        )

        Payment.objects.create(
            user=user,
            date_of_payment="2023-10-02",
            paid_course=None,
            paid_lesson=lesson1,
            amount=3000.00,
            form_of_payment="cash",
        )

        self.stdout.write(self.style.SUCCESS("Данные о платежах успешно загружены!"))
