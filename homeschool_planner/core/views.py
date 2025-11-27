# Import render and define a view for the homepage
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
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
    """
    Per-student progress dashboard:
    - Unassigned lessons
    - Assigned but not completed
    - Completed lessons with grades
    - Line chart of grades
    """
    student = get_object_or_404(Student, pk=student_id)

    # All LessonProgress rows for this student
    assigned_qs = LessonProgress.objects.filter(
        student=student
    ).select_related("lesson")

    # Split into pending + completed
    pending = assigned_qs.filter(completed=False)
    completed = assigned_qs.filter(completed=True).order_by(
        "completed_at",
        "lesson__lesson_date",
        "lesson__created_at"
    )

    # Lessons with NO progress entries → unassigned
    unassigned_lessons = Lesson.objects.exclude(
        student_progress__student=student
    )

    # Only completed with grades
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
