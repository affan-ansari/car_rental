from django import forms
from .models import CAR, CREDIT_CARD,DRIVER,BOOKING, PAYMENT, RENTAL,RETURNCAR

class RegisterCarForm(forms.ModelForm):
    class Meta:
        model = CAR
        fields = '__all__'
        exclude = ['available']

class SearchCarForm(forms.Form):
    reg_no = forms.CharField(label="Registration Number", max_length=25)

class SearchDriverForm(forms.Form):
    CNIC = forms.CharField(label="CNIC", max_length=15)

class RegisterDriverForm(forms.ModelForm):
    class Meta:
        model = DRIVER
        fields = '__all__'
        exclude = ['available']

class DriverUpdateForm(forms.ModelForm):
    CNIC =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    first_name =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    last_name =  forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    class Meta:
        model = DRIVER
        fields = '__all__'
        exclude = ['available']

class CarUpdateForm(forms.ModelForm):
    # reg_no = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    # car_model = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    # make = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    # model = forms.IntegerField(widget=forms.NumberInput(attrs={'readonly':'True'}))
    # body_type = forms.CharField(widget=forms.TextInput(attrs={'readonly':'True'}))
    class Meta:
        model = CAR
        fields = ['color','fuel','image','fare','accident_details']
        # exclude = ['available','car_model']

class BookCarForm(forms.ModelForm):
    class Meta:
        model = BOOKING
        fields = ['start_date_time','end_date_time','pickup_location','is_driver_needed']

class RentalCarForm(forms.ModelForm):
    class Meta:
        model = RENTAL
        fields = ['date_of_delivery']

class ReturnCarForm(forms.ModelForm):
    class Meta:
        model = RETURNCAR
        fields = '__all__'

class PaymentOptionForm(forms.Form):
    PAYMENT_CHOICES = (
        ('CreditCard','CreditCard'),
        ('Cash','Cash'),
    )
    payment_option = forms.CharField(label="Payment Option",widget=forms.Select(choices=PAYMENT_CHOICES),max_length=30)
    # payment_option = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.RadioSelect,label="Payment Choice")

class PaymentbyCashForm(forms.ModelForm):
    class Meta:
        model = PAYMENT
        fields = '__all__'
        exclude = ['credit_card','balance']

class PaymentbyCreditCardForm(forms.ModelForm):
    #  amount = forms.IntegerField()
    payment_date = forms.DateField()
    class Meta:
        model = CREDIT_CARD
        fields = '__all__'
