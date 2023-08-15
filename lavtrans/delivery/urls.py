from django.urls import include, path
from .views import *

urlpatterns = [
    path('', all_deliveries, name='delivery'),
    path('add_delivery/', add_delivery, name='add_delivery'),
    path('delivery_info/<int:pk>', delivery_info, name='delivery_info'),
    path('delivery_edit/<int:pk>', delivery_edit, name='delivery_edit'),
]
