from .driver import Driver
from ..models import DRIVER
from django.core.exceptions import ObjectDoesNotExist

class DriverList:
    def __init__(self):
        pass

    def add_driver(self, CNIC,first_name,last_name,email,contact_number,address):
        new_driver = DRIVER(
            CNIC=CNIC,first_name=first_name,last_name=last_name,
            email=email,contact_number=contact_number,address=address
        )
        new_driver.save()

    def delete_driver(self,CNIC):
        try:
            searched_driver = DRIVER.objects.get(CNIC=CNIC)
            searched_driver.delete()
            return True
        except ObjectDoesNotExist:
            return False

    def update_driver(self,CNIC,first_name,last_name,email,contact_number,address):
        update_driver = DRIVER.objects.get(CNIC=CNIC)
        update_driver.CNIC = CNIC
        update_driver.first_name = first_name
        update_driver.last_name = last_name
        update_driver.email = email
        update_driver.contact_number = contact_number
        update_driver.address = address
        update_driver.save()
