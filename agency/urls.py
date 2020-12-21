from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='agency-home'),
    path('manage_cars', views.manage_cars, name='agency-manage-cars'),
    path('register_car', views.register_car, name='agency-register-car'),
    path('delete_car', views.delete_car, name='agency-delete-car'),
    path('car/<str:pk>/', views.CarDetailView.as_view(), name='car-detail'),
    path('manage_drivers', views.manage_drivers, name='agency-manage-drivers'),
    path('register_driver', views.register_driver, name='agency-register-driver'),
    path('delete_driver', views.delete_driver, name='agency-delete-driver'),
    path('update_driver',views.update_driver,name='agency-update-driver'),
]
