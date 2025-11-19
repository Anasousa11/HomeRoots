from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('lessons/', views.lessons, name='lessons'),
    path('progress/', views.progress, name='progress'),
    path('contact/', views.contact, name='contact'),
    path('students/', views.StudentListView.as_view(), name='students'),
    path('students/add/', views.StudentCreateView.as_view(), name='student_add'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
]

