from .driver import Driver
from ..models import DRIVER
from django.core.exceptions import ObjectDoesNotExist

class DriverList:
    def __init__(self):
        pass

    def add_driver(self, CNIC,first_name,last_name,email,contact_number,address,hourly_rate):
        first_name = first_name.title()
        last_name = last_name.title()
        new_driver = Driver(CNIC,first_name,last_name,email,contact_number,address,hourly_rate)
        new_driver.save()

    def delete_driver(self,CNIC):
        try:
            searched_driver = DRIVER.objects.get(CNIC=CNIC)
            if searched_driver.available == False:
                return False
            else:
                searched_driver.available = False
                return True
        except ObjectDoesNotExist:
            return False

    def update_driver(self,CNIC,first_name,last_name,email,contact_number,address,hourly_rate):
        update_driver = self.get_driver(CNIC)
        update_driver.CNIC = CNIC
        update_driver.first_name = first_name.title()
        update_driver.last_name = last_name.title()
        update_driver.email = email
        update_driver.contact_number = contact_number
        update_driver.address = address
        update_driver.hourly_rate = hourly_rate
        update_driver.save()

    def get_drivers(self):
        drivers = DRIVER.objects.filter(available=True)
        return drivers

    def get_driver(self,CNIC):
        try:
            searched_driver = DRIVER.objects.get(CNIC=CNIC)
            if searched_driver.available == False:
                raise Exception(f'{CNIC} was deleted!')
            else:
                return searched_driver
        except ObjectDoesNotExist:
            raise Exception(f'{CNIC} does not exist!')
