from .car import Car
from ..models import CAR
from django.core.exceptions import ObjectDoesNotExist

class CarList:
    def __init__(self):
        pass

    def add_car(self,reg_no,make,model,body_type,engine_capacity,seats,color,transmission,fuel,image):
        reg_no = reg_no.upper()
        new_car = CAR(
            reg_no=reg_no,make=make,model=model,
            body_type=body_type,engine_capacity=engine_capacity,
            seats=seats,color=color,transmission=transmission,fuel=fuel,image=image
        )
        new_car.save()

    def delete_car(self,reg_no):
        reg_no = reg_no.upper()
        try:
            searched_car = CAR.objects.get(reg_no=reg_no)
            searched_car.delete()
            return True
        except ObjectDoesNotExist:
            return False

    def update_car(self,reg_no,make,model,body_type,engine_capacity,seats,color,transmission,fuel,image,accident_details,available):
        update_car = CAR.objects.get(reg_no=reg_no)
        update_car.reg_no = reg_no
        update_car.make = make
        update_car.model = model
        update_car.body_type = body_type
        update_car.engine_capacity = engine_capacity
        update_car.seats = seats
        update_car.color = color
        update_car.transmission = transmission
        update_car.fuel = fuel
        update_car.image = image
        update_car.accident_details = accident_details
        update_car.available = available
        update_car.save()
