from ..models import CAR
class Car:
    def __new__(cls,car_model,reg_no,color,fuel,fare,image):
        new_car = CAR(
        car_model=car_model,
        reg_no=reg_no,
        color=color,
        fuel=fuel,
        fare=fare,
        image=image
        )
        return new_car

    # def __init__(self,car_model,reg_no,color,fuel,fare,image):
    #     new_car = CAR(
    #     car_model=car_model,
    #     reg_no=reg_no,
    #     color=color,
    #     fuel=fuel,
    #     fare=fare,
    #     image=image
    #     )
    #     self.car = new_car

    # def save(self):
    #     self.car.save()
        # return new_car
        # new_car.save()
    #Please visit models.py to see Class.

