from django import forms
from .models import Delivery, DeliveryBack


class AddDeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ('date_of_delivery', 'car', 'driver', 'transporter', 'next_car', 'next_driver',
                  'next_transporter', 'waybill_number', 'waybill_date', 'customer', 'customer_contact',
                  'application_number', 'application_date', 'route', 'rate', 'rate_currency', 'liters',
                  'liters_amount', 'storage', 'customs_clearance', 'customs_currency', 'electronic_seal',
                  'prostoi', 'rate_for_prostoi', 'prostoi_currency', 'score_number', 'score_date',
                  'payment_term', 'score_total', 'score_currency')
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


class AddDeliveryBackForm(forms.ModelForm):
    class Meta:
        model = DeliveryBack
        fields = ('date_of_back_delivery', 'back_customer', 'back_customer_contact', 'back_application_number',
                  'back_application_date', 'back_route', 'back_rate', 'back_rate_currency', 'back_prostoi',
                  'back_rate_for_prostoi', 'back_prostoi_currency', 'back_score_number', 'back_score_date',
                  'back_score_total', 'back_score_currency', 'back_payment_term')
        widgets = {
            'back_route': forms.Textarea(attrs={'rows': 3}),
            'back_customer': forms.TextInput(attrs={'style': 'width: 310px;'}),
            'back_customer_contact': forms.TextInput(attrs={'style': 'width: 310px;'}),
            'back_application_number': forms.TextInput(attrs={'style': 'width: 310px;'}),
            'back_prostoi': forms.NumberInput(attrs={'style': 'width: 310px;'}),
            'back_score_number': forms.TextInput(attrs={'style': 'width: 310px;'}),
            'back_payment_term': forms.NumberInput(attrs={'style': 'width: 310px;'}),
        }
