from rest_framework import serializers
from lms.models import Course, Lesson, Subscription, CoursePayment
from rest_framework import serializers
from lms.validators import validate_link


class LessonSerializer(serializers.ModelSerializer):
    """Валидация."""
    video = serializers.CharField(validators=[validate_link])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    quantity_lessons = serializers.SerializerMethodField()
    info_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ["id", "name", "description", "preview", "quantity_lessons", "info_lessons"]

    def get_quantity_lessons(self, obj):
        """получаем количество уроков"""
        return obj.lesson_set.count()

    def get_info_lessons(self, obj):
        """получаем все уроки связанные с курсом"""
        lessons = obj.lesson_set.all()
        return LessonSerializer(lessons, many=True).data


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = "__all__"


class CoursePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePayment
        fields = "__all__"
