from django.urls import path
from . import views
urlpatterns = [
path('', views.index),
path('index2/<int:val1>/', views.index2),
path('<int:bookId>', views.viewbook),
path('html5/links/', views.links, name='links'),
path('html5/text/formatting/', views.formatting, name='formatting'),
path('html5/listing/', views.listing, name='listing')

]