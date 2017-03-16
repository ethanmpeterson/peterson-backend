from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Student

class UserSerializer(serializers.ModelSerializer):
    #student = serializers.PrimaryKeyRelatedField(many=True, queryset=Student.objects.all())

    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email', 'groups', 'id')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class StudentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Student
        fields = ('grade', 'owner', 'schedule')

class RegistrationSerializer (serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = User
        fields = ('username', 'password')