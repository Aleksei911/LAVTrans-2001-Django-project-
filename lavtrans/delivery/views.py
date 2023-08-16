from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Delivery
from .forms import AddDeliveryForm


@login_required
def all_deliveries(request):
    search_by = request.GET.get('search_by')
    query = request.GET.get('query')

    if query:
        if search_by == "car":
            deliveries = Delivery.objects.filter(car__number__icontains=query)
        elif search_by == "next_car":
            deliveries = Delivery.objects.filter(next_car__number__icontains=query)
        elif search_by == "customer":
            deliveries = Delivery.objects.filter(customer__icontains=query)
    else:
        deliveries = Delivery.objects.all()

    return render(request, 'delivery/delivery.html', {'deliveries': deliveries})


@login_required
def add_delivery(request):
    if request.method == 'POST':
        form = AddDeliveryForm(request.POST)

        if form.is_valid():
            delivery = form.save()
            delivery.save()

            messages.success(request, 'Данные о новой перевозке были успешно добавлены.')

            return redirect('delivery')
    else:
        form = AddDeliveryForm()

    return render(request, 'delivery/add_delivery.html', {'form': form})


@login_required
def delivery_info(request, pk):
    delivery = Delivery.objects.get(pk=pk)

    context = {
        'delivery': delivery,
    }
    return render(request, 'delivery/delivery_info.html', context)


@login_required
def delivery_edit(request, pk):
    delivery = Delivery.objects.get(pk=pk)

    if request.method == 'POST':
        form = AddDeliveryForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()

            messages.success(request, 'Изменения были успешно сохранены.')

            return redirect('delivery_info', pk=pk)
    else:
        form = AddDeliveryForm(instance=delivery)

    return render(request, 'delivery/delivery_edit.html', {'form': form})
