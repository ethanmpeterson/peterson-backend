from django.contrib import admin
from .models import Schedule
from .models import Student
# Register your models here.
admin.site.register(Student)
admin.site.register(Schedule)