from django import forms
from .models import Reservation
from django.utils import timezone
from datetime import datetime
from .widgets import CustomTimeInput
import re


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['nome', 'telefone', 'email', 'data', 'hora']
        widgets = {
            'data': forms.SelectDateWidget(),
            'hora': CustomTimeInput()
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if not nome:
            raise forms.ValidationError('O nome não pode estar vazio.')
        if "'" in nome or '"' in nome:
            raise forms.ValidationError('O nome não pode conter aspas simples ou duplas.')
        return nome

    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if not telefone:
            raise forms.ValidationError('O telefone não pode estar vazio.')
        if not re.match(r'^\d+$', telefone):
            raise forms.ValidationError('O telefone só pode conter números.')
        if "'" in telefone or '"' in telefone:
            raise forms.ValidationError('O telefone não pode conter aspas simples ou duplas.')
        return telefone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('O email não pode estar vazio.')
        if "'" in email or '"' in email:
            raise forms.ValidationError('O email não pode conter aspas simples ou duplas.')
        return email

    def clean_hora(self):
        hora = self.cleaned_data['hora']
        opening_time = timezone.datetime.strptime('09:00:00', '%H:%M:%S').time()
        closing_time = timezone.datetime.strptime('23:00:00', '%H:%M:%S').time()
        if not (opening_time <= hora <= closing_time):
            raise forms.ValidationError('As reservas devem ser efetuadas entre as 09 e as 23 horas .')
        return hora

    def clean_data(self):
        data = self.cleaned_data['data']
        if data < datetime.now().date():
            raise forms.ValidationError('A data da reserva não pode ser no passado.')
        return data

    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('data')
        hora = cleaned_data.get('hora')
        if data and hora:
            # Verifica reservas no mesmo dia e hora
            if Reservation.objects.filter(data=data, hora=hora).exists():
                raise forms.ValidationError('Já existe uma reserva para esta hora.')
        return cleaned_data
