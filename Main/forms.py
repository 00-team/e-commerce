from django import forms
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
    country = CountryField(blank_label="").formfield()
    zip_address = forms.CharField()
    same_billing_addres = forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(),choices=PAYMENT_CHOICES)
