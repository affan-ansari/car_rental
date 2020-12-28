from ..models import CAR_MODEL
class Car_Model:
    def __new__(cls,make,model,body_type,engine_capacity,seats,transmission):
        new_carmodel = CAR_MODEL(
            make=make,
            model=model,
            body_type=body_type,
            engine_capacity=engine_capacity,
            seats=seats,
            transmission=transmission
        )
        return new_carmodel

