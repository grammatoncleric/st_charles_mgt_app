from django.contrib import admin
from django.urls import path
from bookmasses import views 

urlpatterns = [
     path('bookmass', views.bookmass, name='bookmass'),
]