from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name= "books.index"),
path('index2/<int:val1>/', views.index2),
path('html5/links/', views.links, name='links'),
path('html5/text/formatting/', views.formatting, name='formatting'),
path('html5/listing/', views.listing, name='listing'),
path('html5/tables/', views.tables, name='tables'),
path('list_books/', views.list_books, name= "books.list_books"),
path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
path('aboutus/', views.aboutus, name="books.aboutus"),
path('search/', views.search, name="books.search"),
 path('insert_books/', views.insert_books, name='insert_books'),
  path('simple/query/', views.simple_query, name='books.simple_query'),
      path('complex/query/', views.lookup_query, name='books.lookup_query'),
      path('lab8/task1/', views.task1, name='books.task1'),
      path('lab8/task2/', views.task2, name='books.task2'),
      path('lab8/task3/', views.task3, name='books.task3'),
      path('lab8/task4/', views.task4, name='books.task4'),

]