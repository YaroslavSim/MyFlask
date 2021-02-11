<<<<<<< HEAD
"""Views."""
from django.shortcuts import render

from .models import Group, Lecturer, Student


def get_student(request):
    """Student selection function."""
=======
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Lecturer, Group


def get_student(request):
>>>>>>> 4cfba3dede3b2bfbacdfb7fa7509c6476decb442
    students = Student.objects.all().order_by('-first_name')
    return render(request, 'academy/get_student.html', {'students': students})


def get_lecturer(request):
<<<<<<< HEAD
    """Lecturer selection function."""
=======
>>>>>>> 4cfba3dede3b2bfbacdfb7fa7509c6476decb442
    lecturers = Lecturer.objects.all().order_by('-first_name')
    return render(request, 'academy/get_lecturer.html', {'lecturers': lecturers})


def get_group(request):
<<<<<<< HEAD
    """Group selection function."""
    groups = Group.objects.all()
    return render(request, 'academy/get_group.html', {'groups': groups})
=======
    groups = Group.objects.all()
    return render(request, 'academy/get_group.html', {'groups': groups})
>>>>>>> 4cfba3dede3b2bfbacdfb7fa7509c6476decb442
