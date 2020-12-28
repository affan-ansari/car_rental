from ..models import RENTAL

class Rental:
    def __new__(cls,booking,date_of_delivery):
        new_rental = RENTAL(
            booking=booking,
            date_of_delivery=date_of_delivery
        )
        return new_rental