from django import forms
from .models import Car

class RegisterCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'manufacturer', 'year']