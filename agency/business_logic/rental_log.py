from .rental import Rental
from ..models import RENTAL
from django.core.exceptions import ObjectDoesNotExist

class RentalLog:
    def __init__(self):
        pass

    def create_rental(self,booking,date_of_delivery):
        if date_of_delivery >= booking.start_date_time and date_of_delivery < booking.end_date_time:
            new_rental = RENTAL(
                booking=booking,
                date_of_delivery=date_of_delivery
                )
            new_rental.save()
        else:
            print("Raising exception!")
            raise Exception('Car delivery date is not within the booking period!')
