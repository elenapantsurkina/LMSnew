from rest_framework.serializers import ModelSerializer
from lms.models import Course, Lesson
from rest_framework import serializers


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    quantity_lessons = serializers.SerializerMethodField()
    info_lessons = serializers.SerializerMethodField()

    def get_quantity_lessons(self, obj):
        return obj.lesson_set.count()

    def get_info_lessons(self, obj):
        lessons = obj.lesson_set.all()
        return LessonSerializer(lessons, many=True).data

    class Meta:
        model = Course
        fields = ["name", "description", "preview", "quantity_lessons", "info_lessons"]
