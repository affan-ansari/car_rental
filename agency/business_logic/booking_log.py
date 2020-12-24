from .booking import Booking
from ..models import BOOKING
from ..models import CAR
from ..models import DRIVER
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

class BookingLog:
    def __init__(self):
        pass

    def create_booking(self,customer,allocated_car,start_date_time,end_date_time,pickup_location,is_driver_needed):
        if start_date_time > end_date_time:
            raise Exception("Invalid dates! Start Date must be less than End Date!")
        allocated_driver = None
        # raise Exception("Affan gay")
        #Check if driver available on those selected Dates.....
        if is_driver_needed == True:
            allocated_driver = DRIVER.objects.filter(available = True).first()
            try:
                allocated_driver.available = False
                allocated_driver.save()
            except:
               pass
        #  bk = booking
        #  query = (bk.allocated_car == allocated_car) and !{[(bk.st_time > st_time) and (bk.st_time > end_time)] OR [(bk.end_time < st_time) and (bk.end_time < end_time)]}
        current_bookings = BOOKING.objects.filter(
            Q(allocated_car_id=allocated_car.reg_no) &
            ~(
                (Q(start_date_time__gt=start_date_time) & Q(start_date_time__gt=end_date_time)) |
                (Q(end_date_time__lt=start_date_time) & Q(end_date_time__lt=end_date_time))
            )
        ).first()
        # if query returns any bookings, it means the selected car is booked within the range specified by user
        # if current_bookings.exists():
        if current_bookings != None:
            print("Raising exception!")
            raise Exception('Car booked within these dates!')
        else:
            new_booking = BOOKING (
            allocated_car=allocated_car,
            allocated_driver=allocated_driver,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            pickup_location=pickup_location,
            is_driver_needed=is_driver_needed,
            customer=customer
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