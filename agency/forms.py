from django import forms
from .models import Car,Driver

class RegisterCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'reg_no','make', 'model', 'body_type',
            'engine_capacity', 'seats', 'color',
            'transmission', 'fuel'
        ]

class RegisterDriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = [
            'CNIC','first_name','last_name',
            'email', 'contact_number', 'address']

