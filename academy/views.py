"""Views."""
from django.shortcuts import render

from .models import Group, Lecturer, Student

from .forms import StudentForm, LecturerForm, GroupForm


def get_student(request):
    """Student selection function."""
    students = Student.objects.all().order_by('-first_name')
    new_student = None
    if request.method == 'POST':
        student_form = StudentForm(data=request.POST)
        if student_form.is_valid():
            new_student = student_form.save(commit=False)
            new_student.save()
    
    context = {
        'students': students,
        'student_form': StudentForm(),
        'new_student': new_student
    }
    return render(request, 'academy/get_student.html', context)


def get_lecturer(request):
    """Lecturer selection function."""
    lecturers = Lecturer.objects.all().order_by('-first_name')
    new_lecturer = None
    if request.method == 'POST':
        lecturer_form = LecturerForm(data=request.POST)
        if lecturer_form.is_valid():
            new_lecturer = lecturer_form.save(commit=False)
            new_lecturer.save()
    
    context = {
        'lecturers': lecturers,
        'lecturer_form': LecturerForm(),
        'new_lecturer': new_lecturer
    }
    return render(request, 'academy/get_lecturer.html', context)


def get_group(request):
    """Group selection function."""
    groups = Group.objects.all()
    return render(request, 'academy/get_group.html', {'groups': groups})


def new_group(request):
    """Group added function."""
    new_group = None
    if request.method == 'POST':
        group_form = GroupForm(data=request.POST)
        if group_form.is_valid():
            new_group = group_form.save(commit=False)
            new_group.save()
    context = {
        'group_form': GroupForm(),
        'new_group': new_group
    }
    return render(request, 'academy/new_group.html', context)