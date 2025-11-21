from django.db import models
from django.urls import reverse
from django.utils import timezone

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField("Date of birth", null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    notes = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='students/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('core:student_detail', args=[str(self.id)])


class Lesson(models.Model):
    SUBJECT_CHOICES = [
        ('lang', 'Language Arts'),
        ('math', 'Mathematics'),
        ('sci', 'Science'),
        ('ss', 'Social Studies'),
        ('art', 'Arts & Creative'),
        ('pe', 'Physical Education'),
        ('other', 'Other'),
    ]

    LEVEL_CHOICES = [
        ('elem', 'Elementary'),
        ('middle', 'Middle School'),
        ('high', 'High School'),
        ('all', 'All Ages'),
    ]

    title = models.CharField(max_length=150)
    subject = models.CharField(max_length=10, choices=SUBJECT_CHOICES)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    description = models.TextField()
    objectives = models.TextField(help_text="Learning objectives for this lesson")
    materials = models.TextField(blank=True, help_text="Materials and resources needed")
    duration_minutes = models.IntegerField(default=60)
    lesson_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-lesson_date', '-created_at']

    def __str__(self):
        return f"{self.title} ({self.get_subject_display()})"

    def get_absolute_url(self):
        return reverse('core:lesson_detail', args=[str(self.id)])
