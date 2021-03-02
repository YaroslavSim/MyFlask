"""Admin."""
from django.contrib import admin

from .models import Group, Lecturer, Student, Contact

admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Group)
admin.site.register(Contact)