from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),

    # Students
    path('students/', views.students_dashboard, name='students'),
    path('students/list/', views.StudentListView.as_view(), name='student_list'),
    path('students/add/', views.StudentCreateView.as_view(), name='student_add'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),

        #  per-student progress routes
    path(
        'students/<int:student_id>/progress/',
        views.student_progress,
        name='student_progress'
    ),
    path(
        'students/<int:student_id>/progress/assign/<int:lesson_id>/',
        views.assign_lesson,
        name='assign_lesson'
    ),
    path(
        'students/<int:student_id>/progress/complete/<int:lesson_id>/',
        views.mark_lesson_completed,
        name='mark_lesson_completed'
    ),

    # Lessons
    path('lessons/', views.lessons_dashboard, name='lessons'),    
    path('lessons/list/', views.LessonListView.as_view(), name='lesson_list'), 
    path('lessons/add/', views.LessonCreateView.as_view(), name='lesson_add'),
    path('lessons/<int:pk>/', views.LessonDetailView.as_view(), name='lesson_detail'),
    path('lessons/<int:pk>/edit/', views.LessonUpdateView.as_view(), name='lesson_edit'),
    path('lessons/<int:pk>/delete/', views.LessonDeleteView.as_view(), name='lesson_delete'),

    
    # Progress overview 
    path('progress/', views.progress_overview, name='progress_overview'),

    path('contact/', views.contact, name='contact'),
]
