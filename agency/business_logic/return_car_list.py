from ..models import RETURNCAR,RENTAL
from django.core.exceptions import ObjectDoesNotExist

class ReturnCarList:
    def __init__(self):
        pass

    def return_car(self,selected_rental,fine,return_date):
        if return_date <= selected_rental.booking.end_date_time:
            fine.late_return_amount = 0
            fine.save()
        new_returncar = RETURNCAR(
            rental=selected_rental,
            fine = fine,
            return_date=return_date,
            )
        new_returncar.save()
        return new_returncar
    
    def get_returns(self,user):
        if user.is_superuser:
            returns = RETURNCAR.objects.all()
            return returns
        else:
            returns = RETURNCAR.objects.filter(rental__booking__customer = user)
            return returns

    def get_return(self,return_id):
        try:
            car_return = RETURNCAR.objects.get(id=return_id)
            return car_return
        except ObjectDoesNotExist:
            raise Exception(f'Return does not exist!')

    def get_return_by_rental_id(self,rental_id):
        try:
            car_return = RETURNCAR.objects.get(rental__id = rental_id)
            return car_return
        except ObjectDoesNotExist:
            raise Exception(f'Return does not exist!')

