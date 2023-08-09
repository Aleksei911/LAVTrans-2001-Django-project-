from django import forms
from .models import Car, Driver, InsuranceEvent, TechPassport, PassportDriver


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('number', 'model', 'manufacture_year', 'green_card', 'strahovka', 'tehosmotr',
                  'tahograf', 'tamogennoye', 'kasko', 'cmr_strahovka', 'e100_rb', 'e100_rf', 'active')


class AddTechPassportForm(forms.ModelForm):
    class Meta:
        model = TechPassport
        fields = ('vin', 'type_ts', 'category', 'eco_class', 'color', 'engine_capacity',
                  'weight', 'max_weight', 'manufacturer', 'owner', 'price', 'pts', 'pts_date', 'place_of_registration')


class AddDriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ('name', 'last_name', 'middle_name', 'passport', 'visa', 'driver_card', 'mezhdunarodnik', 'chip',
                  'adr', 'doverennost_rus', 'doverennost_lt', 'doverennost_mul', 'active')


class AddPassportDriverForm(forms.ModelForm):
    class Meta:
        model = PassportDriver
        fields = ('date_of_birth', 'passport_number', 'date_of_issue', 'identification_number', 'authority',
                  'place_of_residence')


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
