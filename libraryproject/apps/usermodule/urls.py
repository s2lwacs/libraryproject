from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "users.index"),
    path('insertData/', views.insert_mockup_data, name='insert'),
     path('students-per-city/', views.students_per_city, name='students_per_city'),
]