from django import forms
from .models import Car


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('number', 'green_card', 'strahovka', 'tehosmotr',
                  'tahograf', 'tamogennoye', 'kasko', 'cmr_strahovka', 'active')
