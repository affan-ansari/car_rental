from ..models import Car

def car_list():
    cars = Car.objects.all()
    return cars

def add_car():
    pass
    # TAKE INPUT USING FORMS
    # IF FORM IS VALID SAVE FORM
    # ELSE GO TO REGISTER CAR PAGE AGAIN