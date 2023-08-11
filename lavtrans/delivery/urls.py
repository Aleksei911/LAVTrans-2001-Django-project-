from django.urls import include, path
from .views import *

urlpatterns = [
    path('', all_deliveries, name='delivery'),
]
