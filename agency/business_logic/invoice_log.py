from .booking_log import BookingLog
from .invoice import Invoice
from ..models import INVOICE
from .booking_log import *
from django.core.exceptions import ObjectDoesNotExist

class InvoiceLog:
    def __init__(self):
        pass

    def create_invoice(self,booking_id):
        booking = BookingLog().get_booking(booking_id)
        days_booked = (booking.end_date_time - booking.start_date_time).days + 1
        totalAmount = days_booked * booking.allocated_car.fare.car_fare
        new_invoice = Invoice(booking,days_booked,totalAmount)
        new_invoice.save()
        return new_invoice

    def get_invoice(self,booking_id):
        try:
            invoice = INVOICE.objects.get(booking__id=booking_id)
            return invoice
        except ObjectDoesNotExist:
            raise Exception(f'Invoice does not exist!')

    def get_invoices(self,user):
        if user.is_superuser:
            invoices = INVOICE.objects.all()
            return invoices
        else:
            invoices = INVOICE.objects.filter(booking__customer = user)
            return invoices

    def delete_invoice(self,invoice_id):
        try:
            invoice = INVOICE.objects.get(id=invoice_id)
            invoice.booking.delete()
            invoice.delete()
            return True
        except ObjectDoesNotExist:
            return False