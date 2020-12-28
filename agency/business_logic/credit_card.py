from ..models import CREDIT_CARD

class CreditCard:
    def __new__(cls,card_number,code,expiry_date):
        new_credit_card = CREDIT_CARD(
            card_number=card_number,
            code=code,
            expiry_date=expiry_date
        )
        return new_credit_card