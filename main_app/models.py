from django.db import models
from django.urls import reverse

class Gift(models.Model):
    giftName=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    
        
    def __str__(self):
        return self.giftName

class Birthday(models.Model):
    name=models.CharField(max_length=50)
    date=models.DateField()
    relationship=models.CharField(max_length=30)
    venue=models.CharField(max_length=100)
    gift=models.ManyToManyField(Gift)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'birthdays_id': self.id})


