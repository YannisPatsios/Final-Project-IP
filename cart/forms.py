from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class CheckoutForm(forms.Form):
    address = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Shipping Address', 'class': 'form-control'}))
    country = CountryField().formfield(widget=CountrySelectWidget(attrs={'class': 'form-select'}), required=True)
    phone = forms.CharField(max_length=32, required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone Number (e.g. +1234567890)', 'class': 'form-control'}))

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        import re
        if not re.fullmatch(r'\+?\d{7,15}', phone):
            raise forms.ValidationError('Enter a valid phone number with country code, numbers only.')
        return phone 