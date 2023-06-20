from django.db import models

class student(models.Model):
    name=models.CharField(max_length=50)
    faculty=models.CharField(max_length=50)
    roll=models.IntegerField()
    phone=models.IntegerField()

# Create your models here.
1