from django.shortcuts import render
from .models import Birthday

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birthdays_index(request):
    birthdays = Birthday.objects.all()
    return render(request, 'birthdays/index.html', { 'birthdays': birthdays })