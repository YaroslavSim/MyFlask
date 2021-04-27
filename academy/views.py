"""Views."""
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Group, Lecturer, Student, Contact
from .forms import StudentForm, LecturerForm, GroupForm, ContactForm
from exchanger.models import ExchangeRate
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from hillel_lesson.settings import PER_PAGE
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from academy.serializers import StudentSerializer, GroupSerializer, LecturerSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework import status
from django.http import HttpResponse


def view_student(request):
    """Student selection function."""
    students = Student.objects.all()
    paginator = Paginator(students, PER_PAGE)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    context = {
        'page': page,
        'students': students
    }
    return render(request, 'academy/view_students.html', context)


def view_lecturer(request):
    """Lecturer selection function."""
    lecturers = Lecturer.objects.all()
    paginator = Paginator(lecturers, PER_PAGE)
    page = request.GET.get('page')
    try:
        lecturers = paginator.page(page)
    except PageNotAnInteger:
        lecturers = paginator.page(1)
    except EmptyPage:
        lecturers = paginator.page(paginator.num_pages)
    context = {
        'page': page,
        'lecturers': lecturers
    }
    return render(request, 'academy/view_lecturers.html', context)


def view_group(request):
    """Group selection function."""
    groups = Group.objects.all()
    paginator = Paginator(groups, PER_PAGE)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        groups = paginator.page(1)
    except EmptyPage:
        groups = paginator.page(paginator.num_pages)
    context = {
        'page': page,
        'groups': groups
    }
    return render(request, 'academy/view_groups.html', context)


def add_group(request):
    """Group add function."""
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
    return render(request, 'academy/add_group.html', context)


def edit_students(request):
    """Students edit function."""
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
    return render(request, 'academy/edit_students.html', context)


#@login_required
def edit_student(request, student_id):
    """Student edit function."""
    student = get_object_or_404(Student, student_id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('edit_students')

    form = StudentForm(instance=student)
    return render(request, 'academy/edit_student.html', {'form': form})


def delete_student(request, student_id):
    """Student delete function."""
    student = get_object_or_404(Student, student_id=student_id)
    if student_id:
        student.delete()
        return redirect('edit_students')
    students = Student.objects.all()
    return render(request, 'academy/view_students.html', {'students': students})


def edit_lecturers(request):
    """Lecturers edit function."""
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
    return render(request, 'academy/edit_lecturers.html', context)


def edit_lecturer(request, lecture_id):
    """Lecturer edit function."""
    lecturer = get_object_or_404(Lecturer, lecture_id=lecture_id)
    if request.method == 'POST':
        form = LecturerForm(request.POST, instance=lecturer)
        if form.is_valid():
            lecturer = form.save(commit=False)
            lecturer.save()
            return redirect('edit_lecturers')

    form = LecturerForm(instance=lecturer)
    return render(request, 'academy/edit_lecturer.html', {'form': form})


def delete_lecturer(request, lecture_id):
    """Lecturer delete function."""
    lecturer = get_object_or_404(Lecturer, lecture_id=lecture_id)
    if lecture_id:
        lecturer.delete()
        return redirect('edit_lecturers')
    lecturers = Lecturer.objects.all()
    return render(request, 'academy/view_lecturers.html', {'lecturers': lecturers})


def edit_groups(request):
    """Groups edit function."""
    groups = Group.objects.all()
    new_group = None
    if request.method == 'POST':
        group_form = GroupForm(data=request.POST)
        if group_form.is_valid():
            new_group = group_form.save(commit=False)
            new_group.save()
    context = {
        'groups': groups,
        'group_form': GroupForm(),
        'new_group': new_group
    }
    return render(request, 'academy/edit_groups.html', context)


def edit_group(request, group_id):
    """Group edit function."""
    group = get_object_or_404(Group, group_id=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save(commit=False)
            group.save()
            return redirect('edit_groups')

    form = GroupForm(instance=group)
    return render(request, 'academy/edit_group.html', {'form': form})


def delete_group(request, group_id):
    """Group delete function."""
    group = get_object_or_404(Group, group_id=group_id)
    if group_id:
        group.delete()
        return redirect('edit_groups')
    groups = Group.objects.all()
    return render(request, 'academy/view_groups.html', {'groups': groups})


def contact(request):
    """Contact function."""
    new_contact = None
    sender = request.session.get('sender')
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            new_contact = contact_form.save(commit=False)
            if new_contact.email not in sender:
                new_contact.save()
                if sender:
                    request.session['sender'].append(new_contact.email)
                else:
                    request.session['sender'] = [new_contact.email]
                request.session.modified = True
    context = {
        'contact_form': ContactForm(),
        'new_contact': new_contact,
        'sender': request.session.get('sender')
    }
    return render(request, 'academy/contact.html', context)


def view_contact_message(request):
    """Contact message selection function."""
    contact_messages = Contact.objects.all()
    return render(request, 'academy/view_contact_message.html', {'contact_messages': contact_messages})


def view_exchange_rate(request):
    """Exchange Rate selection function."""
    exchange_rates = ExchangeRate.objects.all()
    context = {
        k: v for ex_rate in exchange_rates
        for k, v in ex_rate.to_dict().items()
    }
    return render(request, 'academy/view_exchange_rate.html', context)


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = 'academy/create_student.html'
    fields = ['first_name', 'last_name', 'email', 'cover']


class StudentEditView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = 'academy/edit_student.html'
    fields = ['first_name', 'last_name', 'email', 'cover']


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'academy/delete_student.html'
    success_url = reverse_lazy('edit_students')


class LecturerCreateView(LoginRequiredMixin, CreateView):
    model = Lecturer
    template_name = 'academy/create_lecturer.html'
    fields = ['first_name', 'last_name', 'email', 'cover']


class LecturerEditView(LoginRequiredMixin, UpdateView):
    model = Lecturer
    template_name = 'academy/edit_lecturer.html'
    fields = ['first_name', 'last_name', 'email', 'cover']


class LecturerDeleteView(LoginRequiredMixin, DeleteView):
    model = Lecturer
    template_name = 'academy/delete_lecturer.html'
    success_url = reverse_lazy('edit_lecturers')


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        rdata = request.data
        data = {
            'first_name': rdata.get('first_name'),
            'last_name': rdata.get('last_name'),
            'email': rdata.get('email')
        }
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def api_student(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    if request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)

    if request.method == 'PUT':
        first_name = request.data.get('first_name')
        if first_name:
            student.first_name = first_name
        last_name = request.data.get('last_name')
        if last_name:
            student.last_name = last_name
        email = request.datatoor.get('email')
        if email:
            student.email = email
        student.save()
        return HttpResponse(status=200)


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def lecturers(request):
    if request.method == 'GET':
        lecturers = Lecturer.objects.all()
        serializer = LecturerSerializer(lecturers, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        rdata = request.data
        data = {
            'first_name': rdata.get('first_name'),
            'last_name': rdata.get('last_name'),
            'email': rdata.get('email')
        }
        serializer = LecturerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def api_lecturer(request, lecturer_id):
    try:
        lecturer = Lecturer.objects.get(pk=lecturer_id)
    except Lecturer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LecturerSerializer(lecturer)
        return Response(serializer.data)

    if request.method == 'DELETE':
        lecturer.delete()
        return HttpResponse(status=204)

    if request.method == 'PUT':
        first_name = request.data.get('first_name')
        if first_name:
            lecturer.first_name = first_name
        last_name = request.data.get('last_name')
        if last_name:
            lecturer.last_name = last_name
        email = request.datatoor.get('email')
        if email:
            lecturer.email = email
        lecturer.save()
        return HttpResponse(status=200)


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def groups(request):
    if request.method == 'GET':
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        rdata = request.data
        data = {
            'course': rdata.get('course'),
            'students': rdata.get('students'),
            'teacher': rdata.get('teacher')
        }
        serializer = GroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def api_group(request, group_id):
    try:
        group = Group.objects.get(pk=group_id)
    except Group.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    if request.method == 'DELETE':
        group.delete()
        return HttpResponse(status=204)

    if request.method == 'PUT':
        course = request.data.get('course')
        if course:
            group.course = course
        students = request.data.get('students')
        if students:
            group.students = students
        teacher = request.datatoor.get('teacher')
        if teacher:
            group.teacher = teacher
        group.save()
        return HttpResponse(status=200)