from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Delivery, DeliveryBack
from .forms import AddDeliveryForm, AddDeliveryBackForm


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
        deliveries = Delivery.objects.order_by('-date_of_delivery')

    return render(request, 'delivery/delivery.html', {'deliveries': deliveries})


@login_required
def add_delivery(request):
    if request.method == 'POST':
        form = AddDeliveryForm(request.POST)
        back_form = AddDeliveryBackForm(request.POST)

        if form.is_valid() and back_form.is_valid():
            delivery = form.save()
            delivery.save()
            back_delivery = back_form.save(commit=False)
            back_delivery.delivery = delivery
            back_delivery.save()

            messages.success(request, 'Данные о новой перевозке были успешно добавлены.')

            return redirect('delivery')
        else:
            print(form.errors)
            print(back_form.errors)
    else:
        form = AddDeliveryForm()
        back_form = AddDeliveryBackForm()

    return render(request, 'delivery/add_delivery.html', {'form': form, 'back_form': back_form})


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
    back_delivery = DeliveryBack.objects.filter(delivery=delivery).first()

    if request.method == 'POST':
        form = AddDeliveryForm(request.POST, instance=delivery)
        if back_delivery:
            back_form = AddDeliveryBackForm(request.POST, instance=back_delivery)
            if form.is_valid() and back_form.is_valid():
                form.save()
                back_form.save()

                messages.success(request, 'Изменения были успешно сохранены.')

                return redirect('delivery_info', pk=pk)
            else:
                print(form.errors)
                print(back_form.errors)
        else:
            back_form = AddDeliveryBackForm(request.POST)
            if form.is_valid() and back_form.is_valid():
                form.save()
                back_delivery_total = back_form.save(commit=False)
                back_delivery_total.delivery = delivery
                back_delivery_total.save()

                messages.success(request, 'Изменения были успешно сохранены.')

                return redirect('delivery_info', pk=pk)
            else:
                print(form.errors)
                print(back_form.errors)
    else:
        if back_delivery:
            form = AddDeliveryForm(instance=delivery)
            back_form = AddDeliveryBackForm(instance=back_delivery)
        else:
            form = AddDeliveryForm(instance=delivery)
            back_form = AddDeliveryBackForm()

    return render(request, 'delivery/delivery_edit.html', {'form': form, 'back_form': back_form})
