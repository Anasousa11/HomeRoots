# Import render and define a view for the homepage
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student, Lesson
from .forms import StudentForm, LessonForm

def index(request):
    return render(request, 'core/index.html')
def students(request):
    return render(request, 'core/students.html')
def lessons(request):
    return render(request, 'core/lessons.html')
def progress(request):
    return render(request, 'core/progress.html')
def contact(request):
    return render(request, 'core/contact.html')

# Student Views
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


# Lesson Views
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
    # core/views.py
from django.shortcuts import render, get_object_or_404
from .models import Student, LessonProgress

def progress_view(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    progress_records = student.lesson_progress.select_related('lesson').all()

    # Filter completed lessons
    completed = progress_records.filter(completed=True)

    # Prepare grade distribution for chart
    grades = [rec.grade for rec in completed if rec.grade is not None]
    grade_counts = {
        'A (80-100)': sum(1 for g in grades if g >= 80),
        'B (60-79)': sum(1 for g in grades if 60 <= g < 80),
        'C (40-59)': sum(1 for g in grades if 40 <= g < 60),
        'D (<40)': sum(1 for g in grades if g < 40),
    }

    context = {
        'student': student,
        'progress_records': progress_records,
        'completed': completed,
        'grade_counts': grade_counts
    }
    return render(request, 'core/progress.html', context)
