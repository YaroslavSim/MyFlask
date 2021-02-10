from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Lecturer, Group


def get_student(request):
    students = Student.objects.all().order_by('-first_name')
    return render(request, 'academy/get_student.html', {'students': students})


def get_lecturer(request):
    lecturers = Lecturer.objects.all().order_by('-first_name')
    return render(request, 'academy/get_lecturer.html', {'lecturers': lecturers})


def get_group(request):
    groups = Group.objects.all()
    return render(request, 'academy/get_group.html', {'groups': groups})