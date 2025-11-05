from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('lessons/', views.lessons, name='lessons'),
    path('progress/', views.progress, name='progress'),
    path('contact/', views.contact, name='contact'),
]
