"""Urls."""
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('students/', views.view_student, name='view_student'),
    path('lecturers/', views.view_lecturer, name='view_lecturer'),
    path('groups/', views.view_group, name='view_group'),
    path('add_group/', views.add_group, name='add_group'),

    path('edit_students/', views.edit_students, name='edit_students'),
    path('students/<int:student_id>/edit/', views.edit_student, name='edit_student'),
    url(r'^delete_student/(?P<student_id>[0-9]+)/$', views.delete_student, name='delete_student'),

    path('edit_lecturers/', views.edit_lecturers, name='edit_lecturers'),
    path('lecturers/<int:lecture_id>/edit/', views.edit_lecturer, name='edit_lecturer'),
    url(r'^delete_lecturer/(?P<lecture_id>[0-9]+)/$', views.delete_lecturer, name='delete_lecturer'),

    path('edit_groups/', views.edit_groups, name='edit_groups'),
    path('groups/<int:group_id>/edit/', views.edit_group, name='edit_group'),
    url(r'^delete_group/(?P<group_id>[0-9]+)/$', views.delete_group, name='delete_group')
]
