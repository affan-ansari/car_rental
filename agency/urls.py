from django.urls import path
from .views import DriverListView
from . import views

urlpatterns = [
    path('', views.home, name='agency-home'),

    path('manage_cars', views.manage_cars, name='agency-manage-cars'),
    path('register_car', views.register_car, name='agency-register-car'),
    path('delete_car', views.delete_car, name='agency-delete-car'),
    path('car/<str:pk>/', views.CarDetailView.as_view(), name='car-detail'),
    path('car/<str:pk>/update/', views.update_car, name='agency-update-car'),
    path('search_car',views.search_car,name='agency-search-car'),

    path('driver/<str:pk>/', views.DriverDetailView.as_view(), name='driver-detail'),
    path('drivers', DriverListView.as_view(),name='agency-drivers-list'),
    path('manage_drivers', views.manage_drivers, name='agency-manage-drivers'),
    path('register_driver', views.register_driver, name='agency-register-driver'),
    path('delete_driver', views.delete_driver, name='agency-delete-driver'),
]

