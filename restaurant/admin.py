from django.contrib import admin
from .models import Reservation, Contact, NewsletterSubscription


# permite mostrar o conteudo de forma... 'tabela'

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'data', 'hora')
    list_filter = ('data', 'hora',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'processado')
    list_filter = ('processado',)


# admin.site.register(NewsletterSubscription)
@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'ativo')
    list_filter = ('ativo',)
