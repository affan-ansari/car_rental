class Booking:
    def __init__(self,allocated_car,allocated_driver,start_date_time,end_date_time,pickup_location,is_driver_needed):
        self.allocated_car = allocated_car
        self.allocated_driver = allocated_driver
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.pickup_location = pickup_location
        self.is_driver_needed = is_driver_needed
