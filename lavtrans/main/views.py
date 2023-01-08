from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/main_page.html')


def about(request):
    return render(request, 'main/about.html')


def transit(request):
    return render(request, 'main/transit.html')


def requisites(request):
    return render(request, 'main/requisites.html')


def contacts(request):
    return render(request, 'main/contacts.html')
