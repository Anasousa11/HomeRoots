# Import render and define a view for the homepage
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm

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