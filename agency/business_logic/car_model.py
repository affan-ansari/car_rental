from ..models import CAR_MODEL
class Car_Model:
    def __init__(self,make,model,body_type,engine_capacity,seats,transmission):
        new_car = CAR_MODEL(
            make=make,
            model=model,
            body_type=body_type,
            engine_capacity=engine_capacity,
            seats=seats,
            transmission=transmission
        )
        return new_car

    