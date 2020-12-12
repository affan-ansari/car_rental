from .car_list import CarList

class Agency:
    def __init__(self):
        self.cars = CarList()

    def add_car(self,reg_no,make,model,body_type,engine_capacity,seats,color,transmission,fuel,image):
        self.cars.add_car(reg_no,make,model,body_type,engine_capacity,seats,color,transmission,fuel,image)
