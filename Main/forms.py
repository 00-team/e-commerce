from django import forms
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField

PAYMENT_CHOICES = (
    ("I","IDPay"),
    ("P","PayPal")
)
class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"1234 Main St"
    }))
    appartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "placeholder": "Apartment or Suite"}))
    country = CountryField(blank_label="").formfield(attrs={
        "class": "custom-select d-block w-100"
    })
    zip_address = forms.CharField(widget=forms.TextInput(attrs={
        "id": "zip"}))
    same_billing_addres = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(),choices=PAYMENT_CHOICES)
