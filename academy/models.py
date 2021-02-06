from django.conf import settings
from django.db import models


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

class Lecturer(models.Model):
    lecture_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    course = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Lecturer, on_delete = models.CASCADE)