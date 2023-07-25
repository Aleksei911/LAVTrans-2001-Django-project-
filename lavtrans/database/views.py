import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import viewsets
from .serializers import CarSerializer, DriverSerializer
from .models import Car, Driver, InsuranceEvent, ImagesInsuranceEvent, TechPassport, TechPassportScans, \
    PassportDriver, DriverScans
from .forms import AddCarForm, AddDriverForm, AddEventForm, ImageForm, AddTechPassportForm, AddPassportDriverForm
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


@login_required
def cars(request):
    search_by = request.GET.get('search_by')
    query = request.GET.get('query')

    if query:
        if search_by == "number":
            cars = Car.objects.filter(number__icontains=query)
    else:
        cars = Car.objects.all()

    return render(request, 'database/cars/cars.html', {'cars': cars})


@login_required
def car_info(request, pk):
    car = Car.objects.get(pk=pk)
    events = InsuranceEvent.objects.filter(car=car)
    techpassport = TechPassport.objects.filter(car=car)

    context = {
        'car': car,
        'events': events,
        'techpassport': techpassport,
    }
    return render(request, 'database/cars/car_detail.html', context)


@login_required
def add_car(request):
    if request.method == 'POST':
        form = AddCarForm(request.POST)

        if form.is_valid():
            car = form.save()
            car.save()

            messages.success(request, 'Новое транспортное средство было успешно добавлено.')
            print(f"{request.user.username} добавил ТС {car.number}")

            return redirect('cars')
    else:
        form = AddCarForm()

    return render(request, 'database/cars/add_car.html', {'form': form})


@login_required
def car_edit(request, pk):
    car = Car.objects.get(pk=pk)

    if request.method == 'POST':
        form = AddCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()

            messages.success(request, 'Изменения были успешно сохранены.')
            print(f"{request.user.username} внес изменения в ТС {car.number} : зелёнка {car.green_card}, "
                  f"страховка {car.strahovka}, техосмотр {car.tehosmotr}, таможенное {car.tamogennoye}, "
                  f"тахограф {car.tahograf}, каско {car.kasko}, смр-страховка {car.cmr_strahovka}, "
                  f"статус {car.active}")

            return redirect('car_info', pk=pk)
    else:
        form = AddCarForm(instance=car)

    return render(request, 'database/cars/edit_car.html', {'form': form})


@login_required
def techpassport_info(request, pk):
    car = Car.objects.get(pk=pk)
    techpassport = TechPassport.objects.get(car=car)
    scans = TechPassportScans.objects.filter(techpassport=techpassport)

    context = {
        'techpassport': techpassport,
        'scans': scans,
    }
    return render(request, 'database/cars/techpassport_info.html', context)


@login_required
def add_techpassport(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddTechPassportForm(request.POST)

        if form.is_valid():
            techpassport = form.save(commit=False)
            techpassport.car = car
            techpassport.save()

            messages.success(request, 'Новые данные были успешно добавлены.')

            return redirect('car_info', pk=pk)
        else:
            print(form.errors)
    else:
        form = AddTechPassportForm()

    return render(request, 'database/cars/add_techpassport.html', {'form': form, 'car': car})


@login_required
def techpassport_edit(request, pk):
    techpassport = TechPassport.objects.get(pk=pk)

    if request.method == 'POST':
        form = AddTechPassportForm(request.POST, instance=techpassport)
        if form.is_valid():
            form.save()

            messages.success(request, 'Изменения были успешно сохранены.')

            return redirect('techpassport_info', pk=pk)
    else:
        form = AddTechPassportForm(instance=techpassport)

    return render(request, 'database/cars/edit_techpassport.html', {'form': form, 'techpassport': techpassport})


@login_required
def add_techpassport_scans(request, pk):
    techpassport = TechPassport.objects.get(pk=pk)

    if request.method == 'POST':
        files = request.FILES.getlist('image')

        for file in files:
            TechPassportScans.objects.create(techpassport=techpassport, image=file)

        messages.success(request, 'Фото были успешно добавлены.')

        return redirect('techpassport_info', pk=pk)
    else:
        form = ImageForm()
    return render(request, 'database/cars/add_scan.html', {'form': form, 'techpassport': techpassport})


@login_required
def drivers(request):
    search_by = request.GET.get('search_by')
    query = request.GET.get('query')

    if query:
        if search_by == "name":
            drivers = Driver.objects.filter(name__icontains=query)
        elif search_by == "last_name":
            drivers = Driver.objects.filter(last_name__icontains=query)
    else:
        drivers = Driver.objects.all()

    return render(request, 'database/drivers/drivers.html', {'drivers': drivers})


@login_required
def driver_info(request, pk):
    driver = Driver.objects.get(pk=pk)
    passport = PassportDriver.objects.filter(driver=driver)
    events = InsuranceEvent.objects.filter(driver=driver)

    context = {
        'driver': driver,
        'events': events,
        'passport': passport,
    }
    return render(request, 'database/drivers/driver_detail.html', context)


@login_required
def add_driver(request):
    if request.method == 'POST':
        form = AddDriverForm(request.POST)

        if form.is_valid():
            driver = form.save()
            driver.save()

            messages.success(request, 'Новый водитель был успешно добавлен.')
            print(f"{request.user.username} добавил водителя {driver.last_name} {driver.name} {driver.middle_name}")

            return redirect('drivers')
    else:
        form = AddDriverForm()

    return render(request, 'database/drivers/add_driver.html', {'form': form})


@login_required
def driver_edit(request, pk):
    driver = Driver.objects.get(pk=pk)

    if request.method == 'POST':
        form = AddDriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()

            messages.success(request, 'Изменения были успешно сохранены.')
            print(f"{request.user.username} внес изменения для водителя "
                  f"{driver.last_name} {driver.name} {driver.middle_name} : паспорт {driver.passport}, "
                  f"виза {driver.visa}, водительское {driver.driver_card}, статус {driver.active}")

            return redirect('driver_info', pk=pk)
    else:
        form = AddDriverForm(instance=driver)

    return render(request, 'database/drivers/edit_driver.html', {'form': form})


@login_required
def passport_driver_info(request, pk):
    driver = Driver.objects.get(pk=pk)
    passport = PassportDriver.objects.get(driver=driver)
    scans = DriverScans.objects.filter(driver=driver)

    context = {
        'passport': passport,
        'scans': scans,
    }
    return render(request, 'database/drivers/passport_info.html', context)


@login_required
def add_passport_driver(request, pk):
    driver = Driver.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddPassportDriverForm(request.POST)

        if form.is_valid():
            passport = form.save(commit=False)
            passport.driver = driver
            passport.save()

            messages.success(request, 'Новые данные были успешно добавлены.')

            return redirect('driver_info', pk=pk)
        else:
            print(form.errors)
    else:
        form = AddPassportDriverForm()

    return render(request, 'database/drivers/add_passport.html', {'form': form, 'driver': driver})


@login_required
def passport_driver_edit(request, pk):
    passport = PassportDriver.objects.get(pk=pk)

    if request.method == 'POST':
        form = AddPassportDriverForm(request.POST, instance=passport)
        if form.is_valid():
            form.save()

            messages.success(request, 'Изменения были успешно сохранены.')

            return redirect('passport_info', pk=pk)
    else:
        form = AddPassportDriverForm(instance=passport)

    return render(request, 'database/drivers/edit_passport.html', {'form': form, 'passport': passport})


@login_required
def event_info(request, pk):
    event = InsuranceEvent.objects.get(pk=pk)
    photos = ImagesInsuranceEvent.objects.filter(insurance_event=event)

    context = {
        'event': event,
        'photos': photos,
    }
    return render(request, 'database/events/event_info.html', context)


@login_required
def add_car_event(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddEventForm(request.POST)
        files = request.FILES.getlist('image')

        if form.is_valid():
            event = form.save(commit=False)
            event.car = car
            event.save()

            for i in files:
                ImagesInsuranceEvent.objects.create(insurance_event=event, image=i)

            messages.success(request, 'Новый страховой случай был успешно добавлен.')
            print(f"{request.user.username} добавил страховой случай {event.id} {event.car} {event.driver}")

            return redirect('cars')
        else:
            print(form.errors)
    else:
        form = AddEventForm()
        imageform = ImageForm()

    return render(request, 'database/events/add_event.html', {'form': form, 'imageform': imageform, 'car': car})


@login_required
def event_edit(request, pk):
    event = InsuranceEvent.objects.get(pk=pk)

    if request.method == 'POST':
        form = AddEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()

            messages.success(request, 'Изменения были успешно сохранены.')
            print(f"{request.user.username} внес изменения в страховой случай {event.car} : водитель {event.driver}, "
                  f"Дата подачи в страховую {event.date_of_submission}, Страховой полис {event.polis_number}, "
                  f"Справка с ГАИ? {event.police_sertificate}, "
                  f"Способ ремонта {event.repair_method}, Страховая насчитала по калькуляции {event.calculation_sum}, "
                  f"Наши расходы по восстановлению (Калькуляция) {event.expenses}, "
                  f"В нашу пользу (Калькуляция) {event.margin}, На какой сервис отправили ТС {event.service_name}, "
                  f"Дата отправки на сервис {event.service_date}, Сумма счета от сервиса {event.service_sum}, "
                  f"Дата передачи документов по ремонту в страховую {event.final_docs}, "
                  f"Дата оплаты от страховой {event.payment_date}")

            return redirect('event_info', pk=pk)
    else:
        form = AddEventForm(instance=event)

    return render(request, 'database/events/edit_event.html', {'form': form, 'event': event})


@login_required
def add_photo(request, pk):
    event = InsuranceEvent.objects.get(pk=pk)

    if request.method == 'POST':
        files = request.FILES.getlist('image')

        for file in files:
            ImagesInsuranceEvent.objects.create(insurance_event=event, image=file)

        messages.success(request, 'Фото были успешно добавлены.')

        return redirect('event_info', pk=pk)
    else:
        form = ImageForm()
    return render(request, 'database/events/add_photo.html', {'form': form, 'event': event})
