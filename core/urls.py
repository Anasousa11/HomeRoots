from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Home
    path('', views.index, name='index'),

    # STUDENT DASHBOARD (default student page)
    path('students/', views.students_dashboard, name='students_dashboard'),

    # Student List (ONLY ONE DEFINITION)
    path('students/list/', views.StudentListView.as_view(), name='students'),

    # Student CRUD
    path('students/add/', views.StudentCreateView.as_view(), name='student_add'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),

    # LESSON DASHBOARD (default lesson page)
    path('lessons/', views.lessons_dashboard, name='lessons_dashboard'),

    # Lesson List
    path('lessons/list/', views.LessonListView.as_view(), name='lessons'),

    # Lesson CRUD
    path('lessons/add/', views.LessonCreateView.as_view(), name='lesson_add'),
    path('lessons/<int:pk>/', views.LessonDetailView.as_view(), name='lesson_detail'),
    path('lessons/<int:pk>/edit/', views.LessonUpdateView.as_view(), name='lesson_edit'),
    path('lessons/<int:pk>/delete/', views.LessonDeleteView.as_view(), name='lesson_delete'),

    # PROGRESS SYSTEM
    path('progress/<int:student_id>/', views.student_progress, name='student_progress'),
    path('progress/<int:student_id>/assign/<int:lesson_id>/', views.assign_lesson, name='assign_lesson'),
    path('progress/<int:student_id>/complete/<int:lesson_id>/', views.mark_lesson_completed, name='mark_lesson_completed'),

    # CONTACT PAGE
    path('contact/', views.contact, name='contact'),
]
