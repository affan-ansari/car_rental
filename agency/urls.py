from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='agency-home'),
    path('register_car', views.register_car, name='agency-register-car'),
    path('register_driver', views.register_driver, name='agency-register-driver'),
]
