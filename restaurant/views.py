from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Reservation, Contact, NewsletterSubscription
import re


def home(request):
    errors = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            validate_email(email)
            NewsletterSubscription.objects.create(email=email)
            return redirect('home')  # Redirect to home after successful submission
        except ValidationError:
            errors['email'] = 'E-mail inválido.'
        except Exception as e:
            errors['email'] = 'Este e-mail já se encontra registado.'

    return render(request, 'home.html', {'errors': errors})


def about(request):
    return render(request, 'about.html', {})


def menu(request):
    return render(request, 'menu.html', {})


def contact(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')

        errors = {}

        # Validate nome
        if not nome:
            errors['nome'] = 'O nome não pode estar vazio.'
        if "'" in nome or '"' in nome:
            errors['nome'] = 'O nome não pode conter aspas simples ou duplas.'

        # Validate telefone
        if not telefone:
            errors['telefone'] = 'O telefone não pode estar vazio.'
        elif not re.match(r'^\d+$', telefone):
            errors['telefone'] = 'O telefone só pode conter números.'
        elif "'" in telefone or '"' in telefone:
            errors['telefone'] = 'O telefone não pode conter aspas simples ou duplas.'

        # Validate email
        if not email:
            errors['email'] = 'O email não pode estar vazio.'
        elif "'" in email or '"' in email:
            errors['email'] = 'O email não pode conter aspas simples ou duplas.'

        # Validate mensagem
        if not mensagem:
            errors['mensagem'] = 'A mensagem não pode estar vazia.'

        if not errors:
            # If no errors, save the data
            contact = Contact(nome=nome, telefone=telefone, email=email, mensagem=mensagem)
            contact.save()
            return redirect('home')
        else:
            # If there are errors, re-render the form with errors
            return render(request, 'contact.html', {'errors': errors, 'form_data': request.POST})

    return render(request, 'contact.html')


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})


def reservation_success(request):
    return render(request, 'reservation_success.html')
