from django.contrib import admin
from django.urls import path
from pages import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('<int:id>', views.print_baptism, name='print_baptism'),

]
