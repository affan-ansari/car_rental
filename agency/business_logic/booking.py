from ..models import BOOKING
class Booking:
    def __new__(cls,allocated_car,allocated_driver,start_date_time,end_date_time,pickup_location,is_driver_needed,customer):
        new_booking = BOOKING(
            allocated_car=allocated_car,
            allocated_driver=allocated_driver,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            pickup_location=pickup_location,
            is_driver_needed=is_driver_needed,
            customer=customer
            )
        return new_booking

    #Please visit models.py to see Class.