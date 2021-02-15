"""Forms."""
from django import forms

from .models import Student, Lecturer, Group


class StudentForm(forms.ModelForm):
    """StudentForm_class."""

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email')


class LecturerForm(forms.ModelForm):
    """LecturerForm_class."""

    class Meta:
        model = Lecturer
        fields = ('first_name', 'last_name', 'email')


class GroupForm(forms.ModelForm):
    """GroupForm_class."""

    class Meta:
        model = Group
        fields = ('course', 'students', 'teacher')