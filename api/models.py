from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    owner = models.ForeignKey('auth.User', related_name='student', on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)

class Schedule(models.Model):
    student = models.ForeignKey('auth.User', related_name='schedule', on_delete=models.CASCADE)

    d1p1 = models.CharField(max_length=150)

