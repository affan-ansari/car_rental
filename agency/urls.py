from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='agency-home'),
    path('register_car', views.register_car, name='agency-register-car'),
    path('register_driver', views.register_driver, name='agency-register-driver'),
    path('manage_cars', views.manage_cars, name='agency-manage-cars'),
    path('manage_drivers', views.manage_drivers, name='agency-manage-drivers'),
    path('delete_car', views.delete_car, name='agency-delete-car'),
]
