from agency.business_logic.return_car import ReturnCarList
from .car_list import CarList
from .driver_list import DriverList
from .booking_log import BookingLog
from .rental_log import RentalLog
from .invoice_log import InvoiceLog
from .payment_log import PaymentLog
from .fines import Fines
from django.utils import timezone
class Agency:
    def __init__(self):
        self.cars = CarList()
        self.drivers = DriverList()
        self.bookings = BookingLog()
        self.rentals = RentalLog()
        self.invoices = InvoiceLog()
        self.payments = PaymentLog()
        self.returns = ReturnCarList()
        self.fines = Fines()

    def add_car(self,car_model,reg_no,color,fuel,fare,image):
        self.cars.add_car(car_model,reg_no,color,fuel,fare,image)

    def add_carmodel(self,make,model,body_type,engine_capacity,seats,transmission):
        self.cars.add_carmodel(make,model,body_type,engine_capacity,seats,transmission)

    def update_car(self,reg_no,color,fuel,image,fare,accident_details):
        self.cars.update_car(reg_no,color,fuel,image,fare,accident_details)

    def delete_car(self,reg_no):
        return self.cars.delete_car(reg_no)

    def browse_cars():
        return self.cars.get_cars()

    def add_driver(self,CNIC,first_name,last_name,email,contact_number,address,hourly_rate):
        self.drivers.add_driver(CNIC,first_name,last_name,email,contact_number,address,hourly_rate)

    def update_driver(self,CNIC,first_name,last_name,email,contact_number,address,hourly_rate):
        self.drivers.update_driver(CNIC,first_name,last_name,email,contact_number,address,hourly_rate)
    
    def delete_driver(self,CNIC):
        return self.drivers.delete_driver(CNIC)

    def book_car(self,customer,allocated_car,start_date_time,end_date_time,pickup_location,is_driver_needed):
        return self.bookings.create_booking(customer,allocated_car,start_date_time,end_date_time,pickup_location,is_driver_needed)

    def receive_car(self,booking_id,date_of_delivery):
        self.rentals.create_rental(booking_id,date_of_delivery)

    def return_car(self,rental_id,accident_details,damages,damages_amount,return_date):
        selected_rental = self.rentals.get_rental(rental_id)
        self.cars.update_accident_details(selected_rental.booking.allocated_car.reg_no,accident_details)
        fine = self.fines.create_fine(selected_rental,damages,damages_amount,return_date)
        return self.returns.return_car(selected_rental,fine,return_date)

    def make_payment(self,booking_id,amount,payment_date,card_number='',code='',expiry_date=timezone.now()):
        self.payments.create_payment(booking_id,amount,payment_date,card_number,code,expiry_date)
    
    def create_invoice(self,booking_id):
        return self.invoices.create_invoice(booking_id)

    def delete_invoice(self,invoice_id):
        return self.invoices.delete_invoice(invoice_id)



