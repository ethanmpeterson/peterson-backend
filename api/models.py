from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    #owner = models.ForeignKey('auth.User', related_name='student', on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

class Schedule(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    # day 1 class holders
    d1p1 = models.CharField(max_length=150)
    d1p2 = models.CharField(max_length=150)
    d1p3 = models.CharField(max_length=150)
    d1p4 = models.CharField(max_length=150)
    # day 2 class holders
    d2p1 = models.CharField(max_length=150)
    d2p2 = models.CharField(max_length=150)
    d2p3 = models.CharField(max_length=150)
    d2p4 = models.CharField(max_length=150)

