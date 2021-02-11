"""Urls."""
from django.urls import path

from . import views

urlpatterns = [
    path('students', views.get_student),
    path('lecturers', views.get_lecturer),
    path('groups', views.get_group)
]
