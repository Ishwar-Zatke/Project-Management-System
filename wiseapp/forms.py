from django import forms
from django.forms import ModelForm
from wiseapp.models import DataStudent


class todoAddForm(ModelForm):
    class Meta:
        model = DataStudent
        fields = ('student_name',
                  'student_email',
                  'student_address',
                  'student_project_type',
                  'student_project_name',
                  'student_project_code',
                  'student_project_fees',)

