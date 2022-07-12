from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Gift(models.Model):
    giftName=models.CharField(max_length=30)
    price=models.IntegerField(default=0)

    def __str__(self):
        return self.giftName
    
    def get_absolute_url(self):
        return reverse('gifts_detail', kwargs={'pk': self.id})

class Birthday(models.Model):
    name=models.CharField(max_length=50)
    date=models.DateField()
    relationship=models.CharField(max_length=30)
    venue=models.CharField(max_length=100)
    gift=models.ManyToManyField(Gift)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'birthdays_id': self.id})


