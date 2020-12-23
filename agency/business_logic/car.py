class Car:
    def __init__(self):
        self.reg_no = str()
        self.make = str()
        self.model = int()
        self.body_type = str()
        self.engine_capacity = int()
        self.seats = int()
        self.color = str()
        self.transmission = str()
        self.fuel = str()

    def set_car(self,reg_no,make,model,body_type,engine_capacity,seats,color,transmission,fuel):
        self.reg_no = reg_no
        self.make = make
        self.model = model
        self.body_type = body_type
        self.engine_capacity = engine_capacity
        self.seats = seats
        self.color = color
        self.transmission = transmission
        self.fuel = fuel
