from ..models import FINES,LATEFINE
from django.core.exceptions import ObjectDoesNotExist

class Fines:
    def __init__(self):
        pass

    def create_fine(self,selected_rental,damages,damages_amount,return_date):
        days_late = (return_date - selected_rental.booking.end_date_time).days
        late_fine = LATEFINE(
            per_day_fine=10,
            days_late=days_late,
            )
        late_return_amount = late_fine.per_day_fine * days_late
        new_fine = FINES(
            damages=damages,
            late_fine=late_fine,
            damages_amount=damages_amount,
            late_return_amount=late_return_amount
        )
        late_fine.save()
        new_fine.save()
        return new_fine