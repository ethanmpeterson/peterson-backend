from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView

from models import Student, Schedule
from serializers import UserSerializer, StudentSerializer, ScheduleSerializer, RegisterSerializer, CreateStudentSerializer

class UserList(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentList(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ScheduleList(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class RegisterView(CreateAPIView):
    model = User
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

class CreateStudent(CreateAPIView):
    model = Student
    serializer_class = CreateStudentSerializer
    permission_classes = (permissions.AllowAny,)


