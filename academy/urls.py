"""Urls."""
from django.urls import path

from django.conf.urls import url

from django.conf.urls import include

from . import views

from django.conf import settings

from django.conf.urls.static import static


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
    url(r'^delete_group/(?P<group_id>[0-9]+)/$', views.delete_group, name='delete_group'),

    url(r'^silk/', include('silk.urls', namespace='silk')),
    path('contact/', views.contact, name='contact'),
    path('view_contact_message/', views.view_contact_message, name='view_contact_message'),
    path('view_exchange_rate/', views.view_exchange_rate, name='view_exchange_rate')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
