from django import forms
from .models import Car

class RegisterCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'reg_no','make', 'model', 'body_type',
            'engine_capacity', 'seats', 'color',
            'transmission', 'fuel'
        ]