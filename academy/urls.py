<<<<<<< HEAD
"""Urls."""
=======
>>>>>>> 4cfba3dede3b2bfbacdfb7fa7509c6476decb442
from django.urls import path

from . import views

urlpatterns = [
    path('students', views.get_student),
    path('lecturers', views.get_lecturer),
    path('groups', views.get_group)
]
