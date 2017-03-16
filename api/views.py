from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, StudentSerializer
from api.models import Student
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    # API endpoint allowing user list to be retrieved or edited
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    # allows one to view groups where permissions are set
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)