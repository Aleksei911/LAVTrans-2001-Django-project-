from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Delivery


@login_required
def all_deliveries(request):
    search_by = request.GET.get('search_by')
    query = request.GET.get('query')

    if query:
        if search_by == "car":
            deliveries = Delivery.objects.filter(car__icontains=query)
    else:
        deliveries = Delivery.objects.all()

    return render(request, 'delivery/delivery.html', {'deliveries': deliveries})
