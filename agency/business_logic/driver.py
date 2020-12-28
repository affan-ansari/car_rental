from ..models import DRIVER
class Driver:
    def __new__(cls, CNIC,first_name,last_name,email,contact_number,address,hourly_rate ):
        new_driver = DRIVER(
            CNIC=CNIC,
            first_name=first_name,
            last_name=last_name,
            email=email,
            contact_number=contact_number,
            address=address,
            hourly_rate=hourly_rate
        )
        return new_driver
    #Please visit models.py to see Class.