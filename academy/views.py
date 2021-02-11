"""Views."""
from django.shortcuts import render

from .models import Group, Lecturer, Student


def get_student(request):
    """Student selection function."""
    students = Student.objects.all().order_by('-first_name')
    return render(request, 'academy/get_student.html', {'students': students})


def get_lecturer(request):
    """Lecturer selection function."""
    lecturers = Lecturer.objects.all().order_by('-first_name')
    return render(request, 'academy/get_lecturer.html', {'lecturers': lecturers})


def get_group(request):
    """Group selection function."""
    groups = Group.objects.all()
    return render(request, 'academy/get_group.html', {'groups': groups})
