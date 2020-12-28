from .rental import Rental
from ..models import RENTAL
from .booking_log import BookingLog
from django.core.exceptions import ObjectDoesNotExist

class RentalLog:
    def __init__(self):
        pass

    # def get_rentals(self,user):
    #     rentals = RENTAL.objects.all()
    #     return rentals
    def get_rental(self,pk):
        try:
            rental = RENTAL.objects.get(id=pk)
            return rental
        except ObjectDoesNotExist:
            raise Exception(f'{pk} does not exist!')



    def get_rentals(self,user):
        if user.is_superuser:
            rentals = RENTAL.objects.all()
            return rentals
        else:
            rentals = RENTAL.objects.filter(booking__customer = user)
            return rentals

    def create_rental(self,booking_id,date_of_delivery):
        booking = BookingLog().get_booking(booking_id)
        if date_of_delivery >= booking.start_date_time and date_of_delivery < booking.end_date_time:
            new_rental = Rental(booking,date_of_delivery)
            new_rental.save()
        else:
            print("Raising exception!")
            raise Exception('Car delivery date is not within the booking period!')

