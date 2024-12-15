from django.shortcuts import render,get_object_or_404
from django.db.models import Count

from django.http import HttpResponse
from .models import Address, Student

# Create your views here.
def index(request):
    return render(request, "bookmodule/index.html")

def insert_mockup_data(request):
    # Mock-up data for Address (Saudi Cities)
    addresses = [
        Address(city="Riyadh"),
        Address(city="Jeddah"),
        Address(city="Dammam"),
        Address(city="Mecca"),
        Address(city="Medina"),
        Address(city="Abha"),
        Address(city="Taif"),
        Address(city="Khobar"),
        Address(city="Tabuk"),
        Address(city="Hail"),
    ]
    # Save all addresses
    for address in addresses:
        address.save()

    # Mock-up data for Students (Saudi Names)
    students = [
        Student(name="Ahmed Al-Saud", age=21, address=addresses[0]),
        Student(name="Fatimah Al-Faisal", age=19, address=addresses[1]),
        Student(name="Mohammed Al-Rashid", age=22, address=addresses[2]),
        Student(name="Sara Al-Harbi", age=20, address=addresses[3]),
        Student(name="Yousef Al-Qahtani", age=23, address=addresses[4]),
        Student(name="Noura Al-Ghamdi", age=18, address=addresses[5]),
        Student(name="Ali Al-Otaibi", age=24, address=addresses[6]),
        Student(name="Aisha Al-Zahrani", age=22, address=addresses[7]),
        Student(name="Hassan Al-Dosari", age=25, address=addresses[8]),
        Student(name="Lama Al-Juhani", age=21, address=addresses[9]),
    ]
    # Save all students
    for student in students:
        student.save()

    return HttpResponse("Mock-up data for  students and cities has been added successfully!")


def students_per_city(request):
    city_data = Address.objects.annotate(student_count=Count('students'))
    return render(request, 'usermodule/students_per_city.html', {'city_data': city_data})

from .forms import StudentForm

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
    return redirect('list_students')