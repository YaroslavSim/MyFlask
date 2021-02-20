"""Signals."""
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Group, Lecturer, Student


@receiver(pre_save, sender=Student)
def capitalize_name_student(sender, instance, **kwargs):
    """Student pre_save function."""
    student = instance
    student.first_name = instance.first_name.capitalize()


@receiver(pre_save, sender=Lecturer)
def capitalize_name_lecturer(sender, instance, **kwargs):
    """Lecturer pre_save function."""
    lecturer = instance
    lecturer.first_name = instance.first_name.capitalize()


@receiver(pre_save, sender=Group)
def capitalize_name_group(sender, instance, **kwargs):
    """Group pre_save function."""
    group = instance
    group.course = instance.course.capitalize()