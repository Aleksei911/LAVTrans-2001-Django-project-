import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import viewsets
from .serializers import CarSerializer, DriverSerializer
from .models import Car, Driver
from .forms import AddCarForm
from django.db.models import Q


# Create your views here.
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.filter(
        Q(tehosmotr__lte=(datetime.date.today() + datetime.timedelta(days=20))) |
        Q(green_card__lte=(datetime.date.today() + datetime.timedelta(days=20))) |
        Q(strahovka__lte=(datetime.date.today() + datetime.timedelta(days=20))) |
        Q(tamogennoye__lte=(datetime.date.today() + datetime.timedelta(days=20))) |
        Q(tahograf__lte=(datetime.date.today() + datetime.timedelta(days=20))) |
        Q(kasko__lte=(datetime.date.today() + datetime.timedelta(days=20))) |
        Q(cmr_strahovka__lte=(datetime.date.today() + datetime.timedelta(days=20))),
        active=True
    )
    serializer_class = CarSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.filter(
        Q(passport__lte=(datetime.date.today() + datetime.timedelta(days=30))) |
        Q(visa__lte=(datetime.date.today() + datetime.timedelta(days=30))) |
        Q(driver_card__lte=(datetime.date.today() + datetime.timedelta(days=30))),
        active=True
    )
    serializer_class = DriverSerializer


def cars(request):
    search_by = request.GET.get('search_by')
    query = request.GET.get('query')

    if query:
        if search_by == "number":
            cars = Car.objects.filter(number__icontains=query)
    else:
        cars = Car.objects.all()

    return render(request, 'database/cars.html', {'cars': cars})


def add_car(request):
    if request.method == 'POST':
        form = AddCarForm(request.POST)

        if form.is_valid():
            car = form.save()
            car.save()

            messages.success(request, 'Новое транспортное средство было успешно добавлено.')

            return redirect('cars')
    else:
        form = AddCarForm()

    return render(request, 'database/add_car.html', {'form': form})


def car_edit(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'POST':
        form = AddCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()

            messages.success(request, 'Изменения были успешно сохранены.')

            return redirect('cars')
    else:
        form = AddCarForm(instance=car)

    return render(request, 'database/edit_car.html', {'form': form})
