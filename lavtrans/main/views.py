from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def index(request):
    return render(request, 'main/main_page.html')


def about(request):
    return render(request, 'main/about.html')


def transit(request):
    return render(request, 'main/transit.html')


def requisites(request):
    return render(request, 'main/requisites.html')


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'message from the website'
            body = {
                'first_name': form.cleaned_data['first_name'],
                'phone_number': form.cleaned_data['phone_number'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = '\n'.join(body.values())
            try:
                send_mail(subject, message,
                          body['email'],
                          ['hoziain@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect('contacts')

    form = ContactForm()
    return render(request, 'main/contacts.html', {'form': form})
