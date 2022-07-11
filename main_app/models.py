from django.db import models

class Birthday(models.Model):
    name=models.CharField(max_length=50)
    date=models.DateField()
    venue=models.CharField(max_length=100)
