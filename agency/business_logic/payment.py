from ..models import PAYMENT

class Payment:
    def __new__(cls,amount,payment_date,credit_card,balance):
        new_payment = PAYMENT(
            amount=amount,
            payment_date=payment_date,
            credit_card=credit_card,
            balance=balance
        )
        return new_payment