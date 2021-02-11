<<<<<<< HEAD
"""Models."""
=======
from django.conf import settings
>>>>>>> 4cfba3dede3b2bfbacdfb7fa7509c6476decb442
from django.db import models


class Student(models.Model):
<<<<<<< HEAD
    """Student class."""

=======
>>>>>>> 4cfba3dede3b2bfbacdfb7fa7509c6476decb442
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

<<<<<<< HEAD

class Lecturer(models.Model):
    """Lecturer class."""

=======
class Lecturer(models.Model):
>>>>>>> 4cfba3dede3b2bfbacdfb7fa7509c6476decb442
    lecture_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

<<<<<<< HEAD

class Group(models.Model):
    """Group class."""

    group_id = models.AutoField(primary_key=True)
    course = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, blank=True)
    teacher = models.ForeignKey(Lecturer, on_delete=models.CASCADE, null=True)
=======
class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    course = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
    teacher = models.ForeignKey(Lecturer, on_delete = models.CASCADE)
>>>>>>> 4cfba3dede3b2bfbacdfb7fa7509c6476decb442
