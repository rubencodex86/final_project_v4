from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Reservation(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    data = models.DateField()
    hora = models.TimeField()

    def clean(self):
        # Verifica se está dentro das horas 'aberto'
        opening_time = timezone.datetime.strptime('09:00:00', '%H:%M:%S').time()
        closing_time = timezone.datetime.strptime('22:00:00', '%H:%M:%S').time()
        if not (opening_time <= self.hora <= closing_time):
            raise ValidationError('Só são aceites reservas entre as 09 e as 23 horas')

    def __str__(self):
        return f"{self.nome} - {self.data} at {self.hora}"


class Contact(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    mensagem = models.TextField()
    processado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} - {self.email}"


class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.email