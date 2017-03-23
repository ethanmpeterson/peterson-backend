from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from models import *
from serializers import *

class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ParentList(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

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

class GetStudent(ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(user=self.request.user)

class GetParent(ListAPIView):
    serializer_class = ParentSerializer

    def get_queryset(self):
        return Parent.objects.filter(user=self.request.user)

# @api_view(['POST'])
# def GetScheduleWithStudentId(request):
#     serializer = GetScheduleSerializer(data=request.data)
#     if serializer.is_valid():
#         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetScheduleWithStudentId(CreateAPIView):
    model = Schedule
    serializer_class = GetScheduleSerializer
    permission_classes = (permissions.AllowAny,)

class CreateStudent(CreateAPIView):
    model = Student
    serializer_class = CreateStudentSerializer
    permission_classes = (permissions.AllowAny,)

class CreateSchedule(CreateAPIView):
    model = Schedule
    serializer_class = CreateScheduleSerializer
    permission_classes = (permissions.AllowAny,)

class CreateParent(CreateAPIView):
    model = Parent
    serializer_class = CreateParentSerializer
    permission_classes = (permissions.AllowAny,)




