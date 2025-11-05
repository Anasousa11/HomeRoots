# Import render and define a view for the homepage
from django.shortcuts import render

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
