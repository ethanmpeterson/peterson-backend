from rest_framework import serializers
from django.contrib.auth.models import User
from models import Student, Schedule


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False, queryset=User.objects.all())
    class Meta:
        model = Student
        fields = ('user', 'id', 'grade')

class ScheduleSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(many=False, queryset=Student.objects.all())
    class Meta:
        model = Schedule
        fields = ('student', 'id', 'd1p1', 'd1p2', 'd1p3', 'd1p4', 'd2p1', 'd2p2', 'd2p3', 'd2p4')
