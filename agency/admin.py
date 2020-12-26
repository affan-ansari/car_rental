from django.contrib import admin
from .models import CAR,DRIVER,BOOKING,RENTAL,FARE,CAR_MODEL,INVOICE,PAYMENT

admin.site.register(CAR)
admin.site.register(DRIVER)
admin.site.register(BOOKING)
admin.site.register(RENTAL)
admin.site.register(FARE)
admin.site.register(CAR_MODEL)
admin.site.register(INVOICE)
admin.site.register(PAYMENT)
# Register your models here.
