from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  page='home'
  return render(request, 'index.html')

def projects(request):
  page='projects'
  return render(request, 'projects.html')