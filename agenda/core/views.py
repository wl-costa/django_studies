from django.shortcuts import render
from core.models import Evento

# Create your views here.

def lista_eventos(request):
    usuario = request.user # Pega o usuário logado no sistema e armazena na variável usuario 
    evento = Evento.objects.filter(usuario=usuario) # Filtra os eventos do usuário logado e armazena na variável evento
    dados = {'eventos': evento} # Cria um dicionário com o evento e armazena na variável dados
    return render(request, 'agenda.html', dados) # Renderiza a página agenda.html com os dados do dicionário