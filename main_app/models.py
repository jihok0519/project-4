from django.db import models
from django.urls import reverse

class Birthday(models.Model):
    name=models.CharField(max_length=50)
    date=models.DateField()
    relationship:models.CharField(max_length=20)
    venue=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'birthday_id': self.id})

class Gift(models.Model):
    name=models.CharField(max_length=30)
    recipient=models.CharField(max_length=50)
    