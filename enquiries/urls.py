from django.contrib import admin
from django.urls import path
from enquiries import views 

urlpatterns = [
     path('enquiry', views.enquiry, name='enquiry'),
]
