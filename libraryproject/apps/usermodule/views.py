from django.contrib import messages
from django.contrib.auth import authenticate
import django.contrib.auth as at
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,get_object_or_404
from django.db.models import Count
from .forms import RegisterForm

from django.http import HttpResponse
from .models import Address, Address2, Gallery, Student, Student2

# Create your views here.
def index(request):
    return render(request, "bookmodule/index.html")

def insert_mockup_data(request):
  
    addresses = [
        Address2(city="Riyadh"),
        Address2(city="Jeddah"),
        Address2(city="Dammam"),
        Address2(city="Mecca"),
        Address2(city="Medina"),
        Address2(city="Abha"),
        Address2(city="Taif"),
        Address2(city="Khobar"),
        Address2(city="Tabuk"),
        Address2(city="Hail"),
    ]
    # Save all addresses
    for address in addresses:
        address.save()

   
    # students = [
    #     Student2(name="Ahmed Al-Saud", age=21, address=addresses[0]),
    #     Student2(name="Fatimah Al-Faisal", age=19, address=addresses[1]),
    #     Student2(name="Mohammed Al-Rashid", age=22, address=addresses[2]),
    #     Student2(name="Sara Al-Harbi", age=20, address=addresses[3]),
    #     Student2(name="Yousef Al-Qahtani", age=23, address=addresses[4]),
    #     Student2(name="Noura Al-Ghamdi", age=18, address=addresses[5]),
    #     Student2(name="Ali Al-Otaibi", age=24, address=addresses[6]),
    #     Student2(name="Aisha Al-Zahrani", age=22, address=addresses[7]),
    #     Student2(name="Hassan Al-Dosari", age=25, address=addresses[8]),
    #     Student2(name="Lama Al-Juhani", age=21, address=addresses[9]),
    # ]
    # Save all students
    # for student in students:
        # student.save()

    return HttpResponse("Mock-up data for  students and cities has been added successfully!")


def students_per_city(request):
    city_data = Address.objects.annotate(student_count=Count('students'))
    return render(request, 'usermodule/students_per_city.html', {'city_data': city_data})

from .forms import GalleryForm, Student2Form, StudentForm

def list_students(request):
    students = Student.objects.select_related('address').all()
    return render(request, 'usermodule/student_list.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return list_students(request)
    else:
        form = StudentForm()
    return render(request, 'usermodule/student_form.html', {'form': form, 'title': 'Add Student'})

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return list_students(request)
    else:
        form = StudentForm(instance=student)
    return render(request, 'usermodule/student_form.html', {'form': form, 'title': 'Edit Student'})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return list_students(request)

def list_students2(request):
    students = Student2.objects.all()
    return render(request, 'usermodule/student2_list.html', {'students': students})

def add_student2(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return list_students2(request)
    else:
        form = Student2Form()

    return render(request, 'usermodule/student2_form.html', {'form': form, 'title': 'Add Student'})

def edit_student2(request, student_id):
    student = get_object_or_404(Student2, id=student_id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return list_students2(request)
    else:
        form = Student2Form(instance=student)

    return render(request, 'usermodule/student2_form.html', {'form': form, 'title': 'Edit Student'})

def delete_student2(request, student_id):
    student = get_object_or_404(Student2, id=student_id)
    student.delete()
    return list_students2(request)


def list_gallery(request):
    images = Gallery.objects.all()
    return render(request, 'usermodule/gallery_list.html', {'images': images})

def add_image(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return list_gallery(request)
    else:
        form = GalleryForm()

    return render(request, 'usermodule/gallery_form.html', {'form': form, 'title': 'Add Image'})


def delete_image(request, image_id):
    image = get_object_or_404(Gallery, id=image_id)
    image.delete()
    return list_gallery(request)

    

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['pw1'])
            user.save()
            messages.success(request, "Registeration Successful .")
    else:
        form = RegisterForm()
    return render(request, 'usermodule/register.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            at.login(request, user)
            messages.success(request, "Login successful.")
    else:
        form = AuthenticationForm()
    return render(request, 'usermodule/login.html', {'form': form})