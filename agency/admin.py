from django.contrib import admin
from .models import CAR,DRIVER,BOOKING,RENTAL,FARE,CAR_MODEL

admin.site.register(CAR)
admin.site.register(DRIVER)
admin.site.register(BOOKING)
admin.site.register(RENTAL)
admin.site.register(FARE)
admin.site.register(CAR_MODEL)
# Register your models here.
