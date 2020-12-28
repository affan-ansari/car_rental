from ..models import FINES
class Fine:
    def __new__(cls,damages,late_fine,damages_amount,late_return_amount):
        new_fine = FINES(
            damages=damages,
            late_fine=late_fine,
            damages_amount=damages_amount,
            late_return_amount=late_return_amount
        )
        return new_fine