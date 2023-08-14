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
