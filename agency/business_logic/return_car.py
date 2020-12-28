from ..models import RETURNCAR

class ReturnCar:
    def __new__(cls,selected_rental,fine,return_date):
        new_returncar = RETURNCAR(
            rental=selected_rental,
            fine = fine,
            return_date=return_date,
        )
        return new_returncar