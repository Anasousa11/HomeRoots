from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Home
    path('', views.index, name='index'),

    # Dashboards
    path('students/dashboard/', views.students_dashboard, name='students_dashboard'),
    path('lessons/dashboard/', views.lessons_dashboard, name='lessons_dashboard'),

    # Students
    path('students/', views.StudentListView.as_view(), name='students'),
    path('students/add/', views.StudentCreateView.as_view(), name='student_add'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),

    # Lessons
    path('lessons/', views.LessonListView.as_view(), name='lessons'),
    path('lessons/add/', views.LessonCreateView.as_view(), name='lesson_add'),
    path('lessons/<int:pk>/', views.LessonDetailView.as_view(), name='lesson_detail'),
    path('lessons/<int:pk>/edit/', views.LessonUpdateView.as_view(), name='lesson_edit'),
    path('lessons/<int:pk>/delete/', views.LessonDeleteView.as_view(), name='lesson_delete'),

    # Progress system
    path('progress/<int:student_id>/', views.student_progress, name='student_progress'),
    path('progress/<int:student_id>/assign/<int:lesson_id>/', views.assign_lesson, name='assign_lesson'),
    path('progress/<int:student_id>/complete/<int:lesson_id>/', views.mark_lesson_completed, name='mark_lesson_completed'),

    # Contact
    path('contact/', views.contact, name='contact'),
]
