<<<<<<< HEAD
"""Admin."""
from django.contrib import admin

from .models import Group, Lecturer, Student

admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Group)
=======
from django.contrib import admin
from .models import Student, Lecturer, Group

admin.site.register(Student)
admin.site.register(Lecturer)
admin.site.register(Group)
>>>>>>> 4cfba3dede3b2bfbacdfb7fa7509c6476decb442
