from django.db import models

# Create your models here.
class Student(models.Model):
    Sno=models.IntegerField()
    Sname=models.CharField(max_length=25)
    Sage=models.IntegerField()
    Sadrs=models.CharField(max_length=200)
