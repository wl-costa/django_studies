from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao') # Exibe o título, data do evento e data de criação do evento no painel de administração do Django
    list_filter = ('titulo', 'data_evento') # Adiciona um filtro por título e data do evento no painel de administração do Django

admin.site.register(Evento, EventoAdmin) # Registra o modelo Evento no painel de administração do Django e aplica as configurações do EventoAdmin
