from ..models import CAR,CAR_MODEL,
class Car:
    def __init__(self,car_model,reg_no,color,fuel,fare,image):
        new_car = CAR(
        car_model=car_model,
        reg_no=reg_no,
        color=color,
        fuel=fuel,
        fare=fare,
        image=image
        )
        return new_car
    #Please visit models.py to see Class.

    