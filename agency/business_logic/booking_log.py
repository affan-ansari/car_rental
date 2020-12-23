from .booking import Booking
from ..models import BOOKING
from ..models import CAR
from ..models import DRIVER
from django.core.exceptions import ObjectDoesNotExist

class BookingLog:
    def __init__(self):
        pass
    
    def create_booking(self,allocated_car,start_date_time,end_date_time,pickup_location,is_driver_needed):
        allocated_driver = None
        if is_driver_needed == True:
            allocated_driver = DRIVER.objects.filter(available = True).first()
            try:    
                allocated_driver.available = False
                allocated_driver.save()
            except:
                pass
            
        new_booking = BOOKING (
        allocated_car=allocated_car,
        allocated_driver=allocated_driver,
        start_date_time=start_date_time,
        end_date_time=end_date_time,
        pickup_location=pickup_location,
        is_driver_needed=is_driver_needed
        )
        new_booking.save()
    
    # def delete_booking(self,book_id):
    #     #book_id = book_id.upper()
    #     try:
    #         searched_booking = BOOKING.objects.get(id=book_id)
    #         searched_booking.delete()
    #         return True
    #     except ObjectDoesNotExist:
    #         return False