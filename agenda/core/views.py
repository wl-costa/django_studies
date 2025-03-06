from django.shortcuts import render
from core.models import Evento

# Create your views here.

def lista_eventos(request):
    evento = Evento.objects.get(id=1)
    response = {'evento': evento} # Cria um dicionário com o evento
    return render(request, 'agenda.html', response)