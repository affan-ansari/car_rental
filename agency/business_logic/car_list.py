from .car import Car
from ..models import CAR,CAR_MODEL
from django.core.exceptions import ObjectDoesNotExist

class CarList:
    def __init__(self):
        pass

    def add_car(self,car_model,reg_no,color,fuel,fare,image):
        reg_no = reg_no.upper()
        color = color.capitalize()
        new_car = CAR(car_model=car_model,reg_no=reg_no,color=color,fuel=fuel,fare=fare,image=image)
        new_car.save()

    def add_carmodel(self,make,model,body_type,engine_capacity,seats,transmission):
        make = make.title()
        new_carmodel = CAR_MODEL(
            make=make,model=model,body_type=body_type,
            engine_capacity=engine_capacity,seats=seats,transmission=transmission
        )
        new_carmodel.save()

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
        searched_car.color = color.capitalize()
        searched_car.fuel = fuel
        searched_car.image = image
        searched_car.accident_details = accident_details
        searched_car.fare = fare
        searched_car.save()

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

    def get_filtered_cars(self,max_fare,color,fuel,body_type,max_engine_capacity,transmission):
        if max_fare == None:
            max_fare = 10000
        if max_engine_capacity == None:
            max_engine_capacity = 10000
        if color == '':
            filtered_cars = CAR.objects.filter(
                fare__car_fare__lte=max_fare,fuel=fuel,
                car_model__body_type=body_type,car_model__transmission=transmission
            )
            return filtered_cars
        else:
            filtered_cars = CAR.objects.filter(
                fare__car_fare__lte=max_fare,fuel=fuel,color=color,
                car_model__body_type=body_type,car_model__transmission=transmission
            )
            return filtered_cars