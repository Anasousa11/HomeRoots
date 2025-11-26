# Import render and define a view for the homepage
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student, Lesson, LessonProgress
from .forms import StudentForm, LessonForm
import json
 

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')


# -----------------------------------------
# DASHBOARD VIEWS
# -----------------------------------------
def students_dashboard(request):
    return render(request, 'core/students/dashboard.html')

def lessons_dashboard(request):
    return render(request, 'core/lessons/dashboard.html')


# -----------------------------------------
# STUDENT VIEWS
# -----------------------------------------
class StudentListView(ListView):
    model = Student
    template_name = 'core/students/list.html'
    context_object_name = 'students'
    paginate_by = 12

class StudentDetailView(DetailView):
    model = Student
    template_name = 'core/students/detail.html'
    context_object_name = 'student'

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


# -----------------------------------------
# LESSON VIEWS
# -----------------------------------------
class LessonListView(ListView):
    model = Lesson
    template_name = 'core/lessons/list.html'
    context_object_name = 'lessons'
    paginate_by = 10

class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'core/lessons/detail.html'
    context_object_name = 'lesson'

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


# -----------------------------------------
# PROGRESS VIEW
# -----------------------------------------
def progress_overview(request):
    students = Student.objects.all()
    students_data = []

    for student in students:
        completed_records = LessonProgress.objects.filter(
            student=student,
            completed=True
        ).select_related('lesson')

        grades = [r.grade for r in completed_records if r.grade is not None]

        grade_counts = {
            'A (80-100)': sum(1 for g in grades if g >= 80),
            'B (60-79)': sum(1 for g in grades if 60 <= g < 80),
            'C (40-59)': sum(1 for g in grades if 40 <= g < 60),
            'D (<40)': sum(1 for g in grades if g < 40),
        }

        students_data.append({
            'student': student,
            'completed': completed_records,
            'labels': json.dumps(list(grade_counts.keys())),
            'data': json.dumps(list(grade_counts.values()))
        })

    return render(request, 'core/progress/overview.html', {
        'students_data': students_data
    })
