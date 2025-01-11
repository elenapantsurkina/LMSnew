from django.contrib import admin

from lms.models import Course, Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "course")
    list_filter = ("course",)
    search_fields = (
        "name",
        "description",
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
