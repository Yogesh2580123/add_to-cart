from django.db import models

# Create your models here.


class Student(models.Model):
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    dob = models.DateField()
    phone = models.CharField(max_length=16)
    mail = models.EmailField()
    gender = models.CharField(max_length=50)
    langauges = models.CharField(max_length=200)
