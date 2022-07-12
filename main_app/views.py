from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Birthday, Gift

import uuid
import boto3

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def birthdays_index(request):
    birthdays = Birthday.objects.filter(user=request.user)
    return render(request, 'birthdays/index.html', {'birthdays': birthdays})


@login_required
def birthdays_detail(request, birthday_id):
    birthday = Birthday.objects.get(id=birthday_id)
    gift_birthday = Gift.objects.exclude(
        id_in=birthday.gift.all().values_list('id'))
    return render(request, 'birthdays/detail.html', {
        'birthday': birthday,
        'gift': gift_birthday,
    })


@login_required
def assoc_gift(request, birthday_id, gift_id):
    Birthday.objects.get(id=birthday_id).gift.add(gift_id)
    return redirect('detail', birthday_id=birthday_id)


@login_required
def assoc_gift_delete(request, birthday_id, gift_id):
    Birthday.objects.get(id=birthday_id).gift.remove(gift_id)
    return redirect('detail', birthday_id=birthday_id)

def signup(request):
    error_messages = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_messages = 'Invalid Info - Please Try Again.'
    form = UserCreationForm()
    context = {
        'form': form,
        'error_messages': error_messages
    }
    return render(request, 'registration/signup.html', context)

class BirthdayCreate(CreateView):
    model = Birthday
    fields = '__all__'
    success_url = '/birthdays/'


class BirthdayUpdate(UpdateView):
    model = Birthday
    fields = ['date', 'relationship', 'venue']


class BirthdayDelete(DeleteView):
    model = Birthday
    success_url = '/birthdays/'

class GiftDetail(LoginRequiredMixin, DetailView):
    model = Gift
    template_name = 'gifts/detail.html'

class GiftCreate(LoginRequiredMixin, CreateView):
    model = Gift
    fields = ['giftName, price']

class GiftUpdate(LoginRequiredMixin, UpdateView):
    model = Gift
    fields = ['giftName, price']

class GiftDelete(LoginRequiredMixin, DeleteView):
    model = Gift
    success_url = '/gifts/'