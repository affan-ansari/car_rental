from .car import Car
from ..models import CAR
from django.core.exceptions import ObjectDoesNotExist

class CarList:
    def __init__(self):
        pass

    def add_car(self,car_model,reg_no,color,fuel,fare,image):
        reg_no = reg_no.upper()
        new_car = CAR(car_model=car_model,reg_no=reg_no,color=color,fuel=fuel,fare=fare,image=image)
        new_car.save()

    def delete_car(self,reg_no):
        reg_no = reg_no.upper()
        try:
            searched_car = CAR.objects.get(reg_no=reg_no)
            # searched_car.delete()
            if searched_car.available == False:
                return False
            else:
                searched_car.available = False
                searched_car.save()
                return True
        except ObjectDoesNotExist:
            return False

    def update_car(self,searched_car,color,fuel,image,fare,accident_details):
        searched_car.color = color
        searched_car.fuel = fuel
        searched_car.image = image
        searched_car.accident_details = accident_details
        searched_car.fare = fare
        searched_car.save()
        # update_car = CAR.objects.get(reg_no=reg_no)
        # update_car.reg_no = reg_no
        # update_car.make = make
        # update_car.model = model
        # update_car.body_type = body_type
        # update_car.engine_capacity = engine_capacity
        # update_car.seats = seats
        # update_car.color = color
        # update_car.transmission = transmission
        # update_car.fuel = fuel
        # update_car.image = image
        # update_car.accident_details = accident_details
        # update_car.available = available
        # update_car.save()

    def get_cars(self):
        cars = CAR.objects.filter(available=True)
        return cars

    def get_car(self,reg_no):
        try:
            searched_car = CAR.objects.get(reg_no=reg_no)
            if searched_car.available == False:
                raise Exception(f'{reg_no} was deleted!')
            else:
                return searched_car
        except ObjectDoesNotExist:
            raise Exception(f'{reg_no} does not exist!')