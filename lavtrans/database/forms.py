from django import forms
from django.contrib.admin import widgets
from .models import Car, Driver, ImagesInsuranceEvent, InsuranceEvent


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('number', 'green_card', 'strahovka', 'tehosmotr',
                  'tahograf', 'tamogennoye', 'kasko', 'cmr_strahovka', 'active')


class AddDriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('name', 'last_name', 'middle_name', 'passport', 'visa', 'driver_card', 'active')


class AddEventForm(forms.ModelForm):
    class Meta:
        model = InsuranceEvent
        fields = ('driver', 'date_of_submission', 'polis_number',
                  'police_sertificate', 'repair_method', 'calculation_sum', 'expenses', 'service_name',
                  'service_date', 'service_sum', 'final_docs', 'payment_date')

        date_of_submission = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))


class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label='image',
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )

    class Meta:
        model = ImagesInsuranceEvent
        fields = ('image',)
