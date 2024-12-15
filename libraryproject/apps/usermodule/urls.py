from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "users.index"),
    path('insertData/', views.insert_mockup_data, name='insert'),
     path('students-per-city/', views.students_per_city, name='students_per_city'),
         path('students/', views.list_students, name='list_students'),

     path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
]