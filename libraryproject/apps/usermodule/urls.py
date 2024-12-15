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
      path('students2/', views.list_students2, name='list_students2'),
    path('students2/add/', views.add_student2, name='add_student2'),
    path('students2/edit/<int:student_id>/', views.edit_student2, name='edit_student2'),
    path('students2/delete/<int:student_id>/', views.delete_student2, name='delete_student2'),
     path('gallery/', views.list_gallery, name='list_gallery'),
    path('gallery/add/', views.add_image, name='add_image'),
    path('gallery/delete/<int:image_id>/', views.delete_image, name='delete_image'),
]