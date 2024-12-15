from django import forms
from .models import Student,Student2, Address,Address2

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter student age'}),
            'address': forms.Select(attrs={'class': 'form-control'}),
        }
class Student2Form(forms.ModelForm):
    addresses = forms.ModelMultipleChoiceField(
        queryset=Address2.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter student age'}),
        }