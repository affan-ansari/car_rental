from ..models import INVOICE

class Invoice:
    def __new__(cls,booking,days_booked,totalAmount):
        new_invoice = INVOICE(
            booking=booking,
            days_booked=days_booked,
            totalAmount=totalAmount
        )
        return new_invoice