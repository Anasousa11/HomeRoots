from django import forms
from .models import Student, Lesson

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'dob', 'gender', 'profile_image', 'notes']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'subject', 'level', 'description', 'objectives', 'materials', 'duration_minutes', 'lesson_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lesson title'}),
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'level': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Brief description of the lesson'}),
            'objectives': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'What students will learn...'}),
            'materials': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'List materials, resources, links...'}),
            'duration_minutes': forms.NumberInput(attrs={'class': 'form-control', 'min': '5', 'max': '480'}),
            'lesson_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
