from django.contrib.auth import get_user_model
from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView

from serializers import RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework import status

from api.serializers import UserSerializer, GroupSerializer, StudentSerializer
from api.models import Student
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class UserList(viewsets.ModelViewSet):
    # API endpoint allowing user list to be retrieved or edited
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    # allows one to view groups where permissions are set
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class StudentList(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# @api_view(['POST'])
# def register(request): # create seperate view function for creating user as the serializer above will not show or retrieve the password
#     serial = UserSerializer(data=request.POST)
#     if serial.is_valid():
#         userData = utils.get
#         return Response(serial.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistrationView(CreateAPIView):
    model = User
    serializer_class = RegistrationSerializer
    permission_classes = (permissions.AllowAny,)