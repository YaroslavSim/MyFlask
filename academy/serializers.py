from rest_framework import serializers
from .models import Student, Lecturer, Group


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('student_id', 'first_name', 'last_name', 'email', 'cover')


class LecturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecturer
        fields = ('lecture_id', 'first_name', 'last_name', 'email', 'cover')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('group_id', 'course', 'students', 'teacher')
