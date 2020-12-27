from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.urls import reverse
from PIL import Image
from .business_logic.car import Car
from users.models import User
# class CARMODEL(models.Model):

class FARE(models.Model):
    TYPE_CHOICES = (
        ('Economy','ECONOMY'),
        ('Business','BUSINESS'),
        ('Luxury','LUXURY'),
    )
    car_type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    car_fare = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.car_type + ': $' + str(self.car_fare)

class CAR_MODEL(models.Model):
    BODY_CHOICES = (
        ('HATCHBACK', 'HATCHBACK'),
        ('SEDAN', 'SEDAN'),
        ('COUPE', 'COUPE'),
        ('STATION WAGON', 'STATION WAGON'),
        ('CONVERTABLE', 'CONVERTABLE'),
    )
    TRANSMISSION_CHOICES = (
        ('MANUAL', 'MANUAL'),
        ('AUTOMATIC', 'AUTOMATIC'),
    )
    make = models.CharField(max_length=100)
    model = models.PositiveIntegerField()
    body_type = models.CharField(max_length=100, choices=BODY_CHOICES)
    engine_capacity = models.PositiveIntegerField()
    seats = models.PositiveIntegerField()
    transmission = models.CharField(max_length=100,choices=TRANSMISSION_CHOICES)

    class Meta:
        unique_together = ('make','model')
        verbose_name = 'Car Model'

    def __str__(self):
        return str(self.id) + ': ' + self.make + ' ' + str(self.model)

class CAR(models.Model):
    FUEL_CHOICES = (
        ('PETROL', 'PETROL'),
        ('DIESEL', 'DIESEL'),
    )

    car_model = models.ForeignKey(CAR_MODEL,on_delete=models.PROTECT)
    reg_no = models.CharField(max_length=25,primary_key=True, default="")
    color = models.CharField(max_length=100)
    fuel = models.CharField(max_length=100,choices=FUEL_CHOICES)
    image = models.ImageField(default='default_car.png', upload_to='car_pics')
    fare = models.ForeignKey(FARE,null=True,on_delete=models.PROTECT)
    accident_details = models.TextField(blank=True, default='')
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.car_model.make + ' ' + str(self.car_model.model)

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
    #completed = models.BooleanField() IF TABBY SAY WE DO marjao........
    #invoice... !!! NOT PAYMENT!!!!! INVOICE HAS PAYMENT IN IT.
    #payment_received = models.BooleanField(default=False)
    #payment = models.OnetoOneField(Payment,blah blah)
    def __str__(self):
        #return 'Booking:' + str(self.id) + self.allocated_car
        return 'Booking:' + str(self.id) + ' Customer:' + str(self.customer.pk)

class RENTAL(models.Model):
    booking = models.OneToOneField(BOOKING,on_delete=models.PROTECT,related_name='rentals')
    date_of_delivery = models.DateTimeField()
    #driver_delivery = models.BooleanField() # Needed or not?

class CREDIT_CARD(models.Model):
    card_number = models.CharField(max_length=25,default="")
    code = models.CharField(max_length=4,default="")
    expiry_date = models.DateField()

    def __str__(self):
        return self.card_number


class PAYMENT(models.Model):
    amount = models.PositiveIntegerField(default=0)
    payment_date = models.DateField()
    credit_card = models.ForeignKey(CREDIT_CARD,null=True,on_delete=models.PROTECT)
    balance = models.PositiveIntegerField(default=0)
    def __str__(self):
        return 'Payment:' + str(self.id) + 'CreditCard:' + str(self.credit_card)

class INVOICE(models.Model):
    payment = models.OneToOneField(PAYMENT,null=True,on_delete=models.CASCADE)
    booking = models.OneToOneField(BOOKING,null=True,on_delete=models.CASCADE)
    totalAmount = models.PositiveIntegerField(default=0)
    days_booked = models.PositiveIntegerField(default=0)

class LATEFINE(models.Model):
    per_day_fine = models.PositiveIntegerField(default=10)
    days_late = models.PositiveIntegerField(default=0)

# class DAMAGES(models.Model):
#     DAMAGE_TYPE = (
#         ('Mechanical','Mechanical'),
#         ('Body Damage','Body Damage'),
#     )
#     type = models.CharField(max_length=15,null=True,choices=DAMAGE_TYPE)

class FINES(models.Model):
    damages = models.TextField(blank=True, default='')
    late_fine = models.OneToOneField(LATEFINE,null=True,on_delete=models.PROTECT)
    damages_amount = models.PositiveIntegerField(default=0)
    late_return_amount = models.PositiveIntegerField(default=0)

class RETURNCAR(models.Model):
    rental = models.OneToOneField(RENTAL,null=True,on_delete=models.PROTECT)
    return_date = models.DateTimeField()
    fine = models.OneToOneField(FINES,null=True,on_delete=models.PROTECT)
