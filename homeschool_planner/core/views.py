# Import render and define a view for the homepage
from django.shortcuts import render

def index(request):
	return render(request, 'core/base.html')
