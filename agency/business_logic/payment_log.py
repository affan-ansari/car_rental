from ..models import CREDIT_CARD, PAYMENT,INVOICE
from .invoice_log import InvoiceLog
from .payment import Payment
from .credit_card import CreditCard
from django.core.exceptions import ObjectDoesNotExist

class PaymentLog:
    def __init__(self):
        pass

    def create_credit_card(self,card_number,code,expiry_date):
        new_credit_card = CreditCard(card_number,code,expiry_date)
        new_credit_card.save()
        return new_credit_card

    def create_payment(self,booking_id,amount,payment_date,card_number,code,expiry_date):
        invoice = InvoiceLog().get_invoice(booking_id)
        if card_number == '':
            credit_card = None
            balance = amount - invoice.totalAmount
            new_payment = Payment(amount,payment_date,credit_card,balance)
            new_payment.save()
            invoice.payment = new_payment
            invoice.save()
        else:
            credit_card = self.create_credit_card(card_number,code,expiry_date)
            balance = 0
            new_payment = Payment(invoice.totalAmount,payment_date,credit_card,balance)
            new_payment.save()
            invoice.payment = new_payment
            invoice.save()