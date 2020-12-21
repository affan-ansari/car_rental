from django.db import models
from django.urls import reverse
from PIL import Image

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

    def __str__(self):
        return self.make + ' ' + str(self.model)

    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'pk': self.reg_no})

class DRIVER(models.Model):
    CNIC = models.CharField(max_length=15)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name