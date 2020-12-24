from django.db import models
from django.urls import reverse
from PIL import Image
from .business_logic.car import Car
from users.models import User

class CAR(models.Model):
    BODY_CHOICES = (
        ('SDN', 'SEDAN'),
        ('CPE', 'COUPE'),
        ('STW', 'STATION WAGON'),
        ('HTB', 'HATCHBACK'),
        ('CNV', 'CONVERTABLE'),
    )
    TRANSMISSION_CHOICES = (
        ('MAN', 'MANUAL'),
        ('AUT', 'AUTOMATIC'),
    )
    FUEL_CHOICES = (
        ('PET', 'PETROL'),
        ('DSL', 'DIESEL'),
    )
    reg_no = models.CharField(max_length=25,primary_key=True, default="")
    make = models.CharField(max_length=100)
    model = models.PositiveIntegerField()
    body_type = models.CharField(max_length=100, choices=BODY_CHOICES)
    engine_capacity = models.PositiveIntegerField()
    seats = models.PositiveIntegerField()
    color = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100,choices=TRANSMISSION_CHOICES)
    fuel = models.CharField(max_length=100,choices=FUEL_CHOICES)
    image = models.ImageField(default='default_car.png', upload_to='car_pics')
    accident_details = models.TextField(blank=True, default='')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.make + ' ' + str(self.model)

    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'pk': self.reg_no})

class DRIVER(models.Model):
    CNIC = models.CharField(max_length=15, primary_key=True, default="")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    hourly_rate = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class BOOKING(models.Model):
    allocated_car = models.ForeignKey(CAR,null=True,on_delete=models.PROTECT)
    allocated_driver = models.ForeignKey(DRIVER,null=True,on_delete=models.PROTECT)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    pickup_location = models.TextField(blank=True, default='')
    is_driver_needed = models.BooleanField()
    customer = models.ForeignKey(User,on_delete=models.PROTECT)

    def __str__(self):
        #return 'Booking:' + str(self.id) + self.allocated_car
        return 'Booking:' + str(self.id) + ' Customer:' + str(self.customer.pk)
