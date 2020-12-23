from .car_list import CarList
from .driver_list import DriverList

class Agency:
    def __init__(self):
        self.cars = CarList()
        self.drivers = DriverList()

    def add_car(self,reg_no,make,model,body_type,engine_capacity,seats,color,transmission,fuel,image):
        self.cars.add_car(reg_no,make,model,body_type,engine_capacity,seats,color,transmission,fuel,image)

    def delete_car(self,reg_no):
        return self.cars.delete_car(reg_no)

    def update_car(self,reg_no,make,model,body_type,engine_capacity,seats,color,transmission,fuel,image,accident_details,available):
        self.cars.update_car(reg_no,make,model,body_type,engine_capacity,seats,color,transmission,fuel,image,accident_details,available)

    def add_driver(self,CNIC,first_name,last_name,email,contact_number,address,hourly_rate):
        self.drivers.add_driver(CNIC,first_name,last_name,email,contact_number,address,hourly_rate)

    def delete_driver(self,CNIC):
        return self.drivers.delete_driver(CNIC)

    def update_driver(self,CNIC,first_name,last_name,email,contact_number,address,hourly_rate):
        self.drivers.update_driver(CNIC,first_name,last_name,email,contact_number,address,hourly_rate)
