from django import forms
from .models import Student,Student2, Address,Address2
from django.contrib.auth.models import User

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
from .models import Gallery

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
        }




class RegisterForm(forms.ModelForm):
    pw1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    pw2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        passw1 = cleaned_data.get('pw1')
        passw2 = cleaned_data.get('pw2')
        if passw1 and passw2 and passw1 != passw2:
            self.add_error('pw2', 'Passwords do not match.')
        return cleaned_data
