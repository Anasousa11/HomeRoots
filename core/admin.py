from django.contrib import admin
from .models import Student, Lesson

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob', 'created_at')
    search_fields = ('first_name', 'last_name')
    list_filter = ('gender',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'level', 'lesson_date', 'duration_minutes')
    search_fields = ('title', 'description')
    list_filter = ('subject', 'level', 'lesson_date')
