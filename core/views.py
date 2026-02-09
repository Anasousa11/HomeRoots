# Import render and define a view for the homepage
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Student, Lesson, LessonProgress
from .forms import StudentForm, LessonForm
from django.contrib import messages
from django.core.mail import send_mail
import json

 
def index(request):
    return render(request, 'core/index.html')


# -----------------------------------------
# AUTHENTICATION VIEWS
# -----------------------------------------
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = 'core:index'


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Account created successfully! Please log in.')
        return super().form_valid(form)


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

class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'core/students/form.html'
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, f'Student "{form.cleaned_data["first_name"]} {form.cleaned_data["last_name"]}" created successfully!')
        return super().form_valid(form)

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'core/students/form.html'
    login_url = 'login'

    def form_valid(self, form):
        messages.success(self.request, f'Student "{form.cleaned_data["first_name"]} {form.cleaned_data["last_name"]}" updated successfully!')
        return super().form_valid(form)

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'core/students/confirm-delete.html'
    success_url = reverse_lazy('core:students')
    login_url = 'login'

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        messages.success(self.request, f'Student "{student.first_name} {student.last_name}" deleted successfully!')
        return super().delete(request, *args, **kwargs)


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



# PROGRESS VIEW


def assign_lesson(request, student_id, lesson_id):
    """
    Assign a lesson to a student (creates LessonProgress with completed=False).
    """
    student = get_object_or_404(Student, pk=student_id)
    lesson = get_object_or_404(Lesson, pk=lesson_id)

    LessonProgress.objects.get_or_create(
        student=student,
        lesson=lesson,
        defaults={"completed": False}
    )

    return redirect("core:student_progress", student_id=student.id)


def mark_lesson_completed(request, student_id, lesson_id):
    """
    Mark a lesson as completed for a student, with optional grade.
    (Used by the Bootstrap modal.)
    """
    student = get_object_or_404(Student, pk=student_id)
    lesson = get_object_or_404(Lesson, pk=lesson_id)

    progress, created = LessonProgress.objects.get_or_create(
        student=student,
        lesson=lesson,
    )

    if request.method == "POST":
        grade_raw = request.POST.get("grade", "").strip()

        if grade_raw:
            try:
                progress.grade = int(grade_raw)
            except ValueError:
                progress.grade = None  # ignore invalid input

        progress.completed = True
        progress.completed_at = timezone.now()
        progress.save()

        return redirect("core:student_progress", student_id=student.id)

    # If accessed via GET by mistake, just go back
    return redirect("core:student_progress", student_id=student.id)

def student_progress(request, student_id):
    student = Student.objects.filter(pk=student_id).first()

    if not student:
        return render(request, "core/progress/student_progress.html", {
            "no_data": True
        })

    assigned_qs = LessonProgress.objects.filter(
        student=student
    ).select_related("lesson")

    pending = assigned_qs.filter(completed=False)
    completed = assigned_qs.filter(completed=True).order_by("-completed_at")

    unassigned_lessons = Lesson.objects.exclude(
        student_progress__student=student
    )

    completed_with_grade = completed.exclude(grade__isnull=True)
    grades = [rec.grade for rec in completed_with_grade]

    overall_grade = round(sum(grades) / len(grades), 1) if grades else None

    chart_labels = [rec.lesson.title for rec in completed_with_grade]
    chart_data = grades

    return render(request, "core/progress/student_progress.html", {
        "student": student,
        "pending": pending,
        "completed": completed,
        "unassigned_lessons": unassigned_lessons,
        "overall_grade": overall_grade,
        "chart_labels": json.dumps(chart_labels),
        "chart_data": json.dumps(chart_data),
    })


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject="New Contact Form Submission",
            message=full_message,
            from_email=email,
            recipient_list=["anasousa11081619@gmail.com"],  # shows in console
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("core:contact")

    return render(request, "core/contact.html")
