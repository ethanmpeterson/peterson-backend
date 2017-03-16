from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Student

class UserSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())

    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email', 'groups', 'student', 'schedule', 'id')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class StudentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Student
        fields = ('grade', 'owner', 'schedule')
