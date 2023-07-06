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


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class ImageForm(forms.Form):
    image = MultipleFileField()
