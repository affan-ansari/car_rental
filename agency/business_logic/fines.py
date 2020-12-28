from .late_fine import LateFine
from .fine import Fine

class Fines:
    def __init__(self):
        pass

    def create_fine(self,selected_rental,damages,damages_amount,return_date):
        days_late = (return_date - selected_rental.booking.end_date_time).days
        per_day_fine=10
        late_fine = LateFine(per_day_fine,days_late)
        late_return_amount = late_fine.per_day_fine * days_late
        new_fine = Fine(damages,late_fine,damages_amount,late_return_amount)
        late_fine.save()
        new_fine.save()
        return new_fine