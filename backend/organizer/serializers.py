from rest_framework import serializers
from django.contrib.auth.models import User
from models import Student, Schedule


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'id')


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

class RegisterSerializer(serializers.ModelSerializer): # registration serializer to handle POST requests to make new users
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')