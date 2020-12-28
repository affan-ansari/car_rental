# from agency.business_logic.car_model import Car_Model
from .car import Car
from .car_model import Car_Model
from ..models import CAR,CAR_MODEL
from django.core.exceptions import ObjectDoesNotExist

class CarList:
    def __init__(self):
        pass

    def add_car(self,car_model,reg_no,color,fuel,fare,image):
        reg_no = reg_no.upper()
        color = color.capitalize()
        new_car = Car(car_model,reg_no,color,fuel,fare,image) # will return CAR (model class) from models.py
        new_car.save()

    def add_carmodel(self,make,model,body_type,engine_capacity,seats,transmission):
        make = make.title()
        new_carmodel = Car_Model(make,model,body_type,engine_capacity,seats,transmission) # will return model class from models.py
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

    def update_car(self,reg_no,color,fuel,image,fare,accident_details):
        searched_car = self.get_car(reg_no)
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

    def update_accident_details(self,reg_no,accident_details):
        car = CAR.objects.get(reg_no=reg_no)
        car.accident_details = accident_details
        car.save()

    def get_filtered_cars(self,car_filter):
        filtered_cars = car_filter.qs
        return filtered_cars

