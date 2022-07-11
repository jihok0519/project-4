from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Birthday

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birthdays_index(request):
    birthdays = Birthday.objects.all()
    return render(request, 'birthdays/index.html', { 'birthdays': birthdays })

def birthdays_detail(request, birthday_id):
    birthday = Birthday.objects.get(id=birthday_id)
    return render(request, 'birthdays/detail.html', { 'birthday': birthday })

class BirthdayCreate(CreateView):
    model = Birthday
    fields = '__all__'
    success_url = '/birthdays/'

class BirthdayUpdate(UpdateView):
    model = Birthday
    fields = ['name', 'date', 'relationship', 'venue']

class BirthdayDelete(DeleteView):
    model = Birthday
    success_url = '/birthdays/'