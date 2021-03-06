"""Urls."""
from django.urls import path

from django.conf.urls import url

from django.conf.urls import include

from . import views

from django.conf import settings

from django.conf.urls.static import static

from django.views.decorators.cache import cache_page

from django.urls import re_path

from .views import StudentCreateView, StudentEditView, StudentDeleteView

from .views import LecturerCreateView, LecturerEditView, LecturerDeleteView


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('students/', views.view_student, name='view_student'),
    path('lecturers/', views.view_lecturer, name='view_lecturer'),
    path('groups/', views.view_group, name='view_group'),
    path('add_group/', views.add_group, name='add_group'),
    path('students/new', StudentCreateView.as_view(), name='create_student'),
    path('lecturer/new', LecturerCreateView.as_view(), name='create_lecturer'),

    path('edit_students/', cache_page(60 * 5)(views.edit_students), name='edit_students'),
    path('students/<int:pk>/edit/', StudentEditView.as_view(), name='edit_student'),
    re_path(r'^delete_student/(?P<pk>[0-9]+)/$', StudentDeleteView.as_view(), name='delete_student'),

    path('edit_lecturers/', cache_page(60 * 5)(views.edit_lecturers), name='edit_lecturers'),
    path('lecturers/<int:pk>/edit/', LecturerEditView.as_view(), name='edit_lecturer'),
    re_path(r'^delete_lecturer/(?P<pk>[0-9]+)/$', LecturerDeleteView.as_view(), name='delete_lecturer'),

    path('edit_groups/', cache_page(60 * 5)(views.edit_groups), name='edit_groups'),
    path('groups/<int:group_id>/edit/', views.edit_group, name='edit_group'),
    re_path(r'^delete_group/(?P<group_id>[0-9]+)/$', views.delete_group, name='delete_group'),

    re_path(r'^silk/', include('silk.urls', namespace='silk')),
    path('contact/', views.contact, name='contact'),
    path('view_contact_message/', views.view_contact_message, name='view_contact_message'),
    path('view_exchange_rate/', views.view_exchange_rate, name='view_exchange_rate'),
    path('users/', include('users.urls')),

    path('api/v1/students/', views.students),
    path('api/v1/students/<int:student_id>', views.api_student),

    path('api/v1/lectures/', views.lecturers),
    path('api/v1/lectures/<int:lecturer_id>', views.api_lecturer),

    path('api/v1/groups/', views.groups),
    path('api/v1/groups/<int:group_id>', views.api_group),

    path('api/v1/auth', views.authenticate_user)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
