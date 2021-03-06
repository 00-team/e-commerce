from django import forms
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField

PAYMENT_CHOICES = (
    ("I","IDPay"),
    ("P","PayPal")
)
class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"1234 Main St",
        "class": "ml-3 w-75"
    }))
    appartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "placeholder": "Apartment or Suite",
        "class": "ml-3 w-75" 
        }))
    country = CountryField(blank_label="(select country)").formfield(widget=CountrySelectWidget(attrs={
        "class": "custom-select d-block w-100"
    }))
    zip_address = forms.CharField(widget=forms.TextInput(attrs={
        "id": "zip",
        "class": "form-control"
        }))
    same_billing_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect(),choices=PAYMENT_CHOICES)
