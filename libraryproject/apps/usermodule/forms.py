from django import forms
from .models import Student, Address

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter student age'}),
            'address': forms.Select(attrs={'class': 'form-control'}),
        }
