from django import forms
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
        fields = ('car', 'driver', 'date_of_submission', 'polis_number',
                  'police_sertificate', 'repair_method', 'calculation_sum', 'expenses', 'margin', 'service_name',
                  'service_date', 'service_sum', 'final_docs', 'payment_date')


class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label='image',
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )

    class Meta:
        model = ImagesInsuranceEvent
        fields = ('image',)
