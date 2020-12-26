from ..models import CREDIT_CARD, PAYMENT,INVOICE
from django.core.exceptions import ObjectDoesNotExist

class PaymentLog:
    def __init__(self):
        pass

    def create_credit_card(self,card_number,code,expiry_date):
        new_credit_card = CREDIT_CARD(
            card_number=card_number,
            code=code,
            expiry_date=expiry_date
        )
        new_credit_card.save()
        return new_credit_card

    def create_payment(self,booking_id,amount,payment_date,credit_card):
        invoice = INVOICE.objects.get(booking__id=booking_id)
        if credit_card == None:
            balance = amount - invoice.totalAmount
            new_payment = PAYMENT(
                amount=amount,
                payment_date=payment_date,
                credit_card=credit_card,
                balance=balance
            )
            new_payment.save()
            invoice.payment = new_payment
            invoice.save()
        else:
            new_payment = PAYMENT(
                amount=invoice.totalAmount,
                payment_date=payment_date,
                credit_card=credit_card
            )
            new_payment.save()
            invoice.payment = new_payment
            invoice.save()