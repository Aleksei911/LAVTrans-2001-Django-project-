from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('transit', views.transit, name='transit'),
    path('requisites', views.requisites, name='requisites'),
    path('contacts', views.contacts, name='contacts'),
]