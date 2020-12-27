from django.urls import path
from .views import BookingsDetailsView, DriverListView, RentalsDetailsView, RentalsView, payment_choice
from . import views

urlpatterns = [
    path('', views.home, name='agency-home'),

    path('manage_cars', views.manage_cars, name='agency-manage-cars'),
    path('register_car', views.register_car, name='agency-register-car'),
    path('register_carmodel', views.register_carmodel, name='agency-register-carmodel'),
    path('delete_car', views.delete_car, name='agency-delete-car'),
    path('car/<str:pk>/', views.CarDetailView.as_view(), name='car-detail'),
    path('car/<str:pk>/update/', views.update_car, name='agency-update-car'),
    path('car/<str:pk>/book/', views.book_car, name='agency-book-car'),
    path('search_car',views.search_car,name='agency-search-car'),
    path('browse_cars',views.browse_cars,name='agency-browse-car'),

    path('search_driver',views.search_driver,name='agency-search-driver'),
    path('driver/<str:pk>/update_driver/', views.update_driver, name='agency-update-driver'),
    path('driver/<str:pk>/', views.DriverDetailView.as_view(), name='driver-detail'),
    path('drivers', DriverListView.as_view(),name='agency-drivers-list'),
    path('manage_drivers', views.manage_drivers, name='agency-manage-drivers'),
    path('register_driver', views.register_driver, name='agency-register-driver'),
    path('delete_driver', views.delete_driver, name='agency-delete-driver'),

    path('booking/<str:pk>/',BookingsDetailsView.as_view(),name='booking-detail'),
    path('bookings',views.BookingsView,name='agency-bookings-list'),

    path('booking/<str:pk>/receive_car/',views.receive_car,name='agency-receive-car'),
    path('rental/<str:pk>/',RentalsDetailsView.as_view(),name='rental-detail'),
    path('rentals',views.RentalsView,name='agency-rentals-list'),

    path('booking/<str:pk>/invoice',views.create_invoice,name='agency-create-invoice'),
    path('invoice/<str:pk>/cancel_booking',views.delete_booking,name='agency-cancel-booking'),
    path('invoices',views.show_invoices,name='agency-invoices-list'),
    path('booking/<str:pk>/invoice/payment_choice',views.payment_choice,name='agency-payment-choice'),
    path('booking/<str:pk>/invoice/<str:payment_option>/payment',views.make_payment,name='agency-make-payment'),
]

