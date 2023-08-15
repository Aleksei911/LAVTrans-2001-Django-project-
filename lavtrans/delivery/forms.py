from django import forms
from .models import Delivery


class AddDeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ('date_of_delivery', 'car', 'driver', 'transporter', 'next_car', 'next_driver',
                  'next_transporter', 'waybill_number', 'waybill_date', 'customer', 'customer_contact',
                  'application_number', 'application_date', 'route', 'rate', 'rate_currency', 'liters',
                  'liters_amount', 'storage', 'customs_clearance', 'customs_currency', 'electronic_seal',
                  'prostoi', 'rate_for_prostoi', 'prostoi_currency', 'score_number', 'score_date',
                  'payment_term')
        widgets = {
            'route': forms.Textarea(attrs={'rows': 3}),
            'waybill_number': forms.TextInput(attrs={'style': 'width: 310px;'}),
            'car': forms.Select(attrs={'style': 'width: 310px;'}),
            'driver': forms.Select(attrs={'style': 'width: 310px;'}),
            'transporter': forms.Select(attrs={'style': 'width: 310px;'}),
            'next_car': forms.Select(attrs={'style': 'width: 310px;'}),
            'next_driver': forms.Select(attrs={'style': 'width: 310px;'}),
            'next_transporter': forms.Select(attrs={'style': 'width: 310px;'}),
            'customer': forms.TextInput(attrs={'style': 'width: 310px;'}),
            'customer_contact': forms.TextInput(attrs={'style': 'width: 310px;'}),
            'application_number': forms.TextInput(attrs={'style': 'width: 310px;'}),
            'liters': forms.NumberInput(attrs={'style': 'width: 310px;'}),
            'liters_amount': forms.NumberInput(attrs={'style': 'width: 310px;'}),
            'storage': forms.NumberInput(attrs={'style': 'width: 310px;'}),
            'prostoi': forms.NumberInput(attrs={'style': 'width: 310px;'}),
            'score_number': forms.TextInput(attrs={'style': 'width: 310px;'}),
            'payment_term': forms.NumberInput(attrs={'style': 'width: 310px;'}),
            'electronic_seal': forms.NumberInput(attrs={'style': 'width: 310px;'}),
        }
