# Import render and define a view for the homepage
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student, Lesson, LessonProgress
from .forms import StudentForm, LessonForm
from collections import Counter
import json

def index(request):
    return render(request, 'core/index.html')



# Student Views
class StudentListView(ListView):
    model = Student
    template_name = 'core/students/list.html'
    context_object_name = 'students'
    paginate_by = 12

class StudentDetailView(DetailView):
    model = Student
    template_name = 'core/students/detail.html'
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'core/students/form.html'

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'core/students/form.html'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'core/students/confirm-delete.html'
    success_url = reverse_lazy('core:students')

# Lesson Views
class LessonListView(ListView):
    model = Lesson
    template_name = 'core/lessons/list.html'
    context_object_name = 'lessons'
    paginate_by = 10

class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'core/lessons/detail.html'
    context_object_name = 'lessons'

class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'core/lessons/form.html'

class LessonUpdateView(UpdateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'core/lessons/form.html'

class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = 'core/lessons/confirm-delete.html'
    success_url = reverse_lazy('core:lessons')

# Progress View
def progress_overview(request):
    students = Student.objects.all()
    students_data = []

    for student in students:
        progress_records = LessonProgress.objects.filter(student=student, completed=True)

        grades = [rec.grade for rec in progress_records if rec.grade is not None]

        grade_counts = {
            'A (80-100)': sum(1 for g in grades if g >= 80),
            'B (60-79)': sum(1 for g in grades if 60 <= g < 80),
            'C (40-59)': sum(1 for g in grades if 40 <= g < 60),
            'D (<40)': sum(1 for g in grades if g < 40),
        }

        students_data.append({
            'student': student,
            'grade_labels': json.dumps(list(grade_counts.keys())),
            'grade_values': json.dumps(list(grade_counts.values())),
            'completed': progress_records,
        })

    return render(request, 'core/progress.html', {
        'students_data': students_data
    })
