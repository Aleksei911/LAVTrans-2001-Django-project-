from django.urls import include, path
from .views import *

urlpatterns = [
    path('', all_deliveries, name='delivery'),
    path('add_delivery/', add_delivery, name='add_delivery'),
]
