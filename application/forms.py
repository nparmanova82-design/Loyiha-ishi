from django import forms
from .models import Student

class Form(forms.ModelForm):
    class Meta:
        model=Student
        fields=['ism','familiya','yosh','picture']