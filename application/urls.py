from django.contrib import admin
from django.urls import path,include
from application import views

urlpatterns = [
    path('', views.application, name='application'),
 
    path('card', views.card, name="card"),
    
    path('register', views.register, name='register'),
   
]