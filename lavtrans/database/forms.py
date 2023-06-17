from django import forms
from .models import Car, Driver


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('number', 'green_card', 'strahovka', 'tehosmotr',
                  'tahograf', 'tamogennoye', 'kasko', 'cmr_strahovka', 'active')


class AddDriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('name', 'last_name', 'middle_name', 'passport', 'visa', 'driver_card', 'active')
