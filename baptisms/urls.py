from django.contrib import admin
from django.urls import path
from baptisms import views 

urlpatterns = [
     path('baptism', views.baptism, name='baptism'),
]