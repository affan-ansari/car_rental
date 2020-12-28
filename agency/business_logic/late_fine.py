from ..models import LATEFINE
class LateFine:
    def __new__(cls,per_day_fine,days_late):
        late_fine = LATEFINE(
            per_day_fine=per_day_fine,
            days_late=days_late,
        )
        return late_fine