from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  page='home'
  return render(request, 'index.html')

def about(request):
  page='about'
  return render(request, 'about.html')

def contact(request):
  page='contact'
  return render(request, 'contact.html')

def projects(request):
  page='projects'
  return render(request, 'projects.html')

def styles(request):
  page='styles'
  return render(request, 'styles.html')

