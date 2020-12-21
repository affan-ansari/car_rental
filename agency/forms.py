from django import forms
from .models import CAR,DRIVER

class RegisterCarForm(forms.ModelForm):
    class Meta:
        model = CAR
        fields = [
            'reg_no','make', 'model', 'body_type',
            'engine_capacity', 'seats', 'color',
            'transmission', 'fuel', 'image'
        ]

class SearchCarForm(forms.Form):
    reg_no = forms.CharField(label="Registration Number", max_length=25)

class RegisterDriverForm(forms.ModelForm):
    class Meta:
        model = DRIVER
        fields = [
            'CNIC','first_name','last_name',
            'email', 'contact_number', 'address']
