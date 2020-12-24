from .car_list import CarList
from .driver_list import DriverList
from .booking_log import BookingLog
from .rental_log import RentalLog
class Agency:
    def __init__(self):
        self.cars = CarList()
        self.drivers = DriverList()
        self.bookings = BookingLog()
        self.rentals = RentalLog()

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

    def book_car(self,customer,allocated_car,start_date_time,end_date_time,pickup_location,is_driver_needed):
        self.bookings.create_booking(customer,allocated_car,start_date_time,end_date_time,pickup_location,is_driver_needed)

    def receive_car(self,booking,date_of_delivery):
        self.rentals.create_rental(booking,date_of_delivery)
    # def delete_booking(self,book_id):
    #     return self.bookings.delete_booking(book_id)