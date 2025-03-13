from django.shortcuts import render, redirect # Importa as funções render e redirect do módulo shortcuts
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.http import require_POST
from datetime import datetime, timedelta # Importa a classe datetime e timedelta do módulo datetime
from django.utils import timezone

# Create your views here.

# def index(request):
#     return redirect('/agenda/') # Redireciona para a página agenda.html

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

@require_POST
def submit_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    usuario = authenticate(username=username, password=password)
    if usuario is not None:
        login(request, usuario)
        return redirect('/')
    else:
        messages.error(request, 'Usuário e/ou senha inválidos')
    return redirect('/')

@login_required(login_url='/login/') # Verifica se o usuário está logado, caso não esteja, redireciona para a página de login
def lista_eventos(request):
    usuario = request.user
    data_atual = timezone.now() - timedelta(hours=1) # Pega a data atual e subtrai uma hora
    evento = Evento.objects.filter(usuario=usuario) # Filtra os eventos do usuário logado e armazena na variável evento
    dados = {'eventos': evento} # Cria um dicionário com o evento e armazena na variável dados
    return render(request, 'agenda.html', dados) # Renderiza a página agenda.html com os dados do dicionário

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados) # Renderiza a página evento.html

@login_required(login_url='/login/')
@require_POST
def submit_evento(request): # Função para submeter um evento no banco de dados
    titulo = request.POST.get('titulo')
    data_evento = request.POST.get('data_evento')
    descricao = request.POST.get('descricao')
    usuario = request.user
    id_evento = request.POST.get('id_evento') # Pega o id do evento 
    if id_evento:
        Evento.objects.filter(id=id_evento).update(titulo=titulo,
                                                   data_evento=data_evento,
                                                   descricao=descricao) # Filtra o evento pelo id e atualiza
    else:
        Evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              descricao=descricao,
                              usuario=usuario) # Cria um evento no banco de dados
    return redirect('/') # Redireciona para a página principal

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete() # Filtra o evento pelo id e deleta
    return redirect('/') # Redireciona para a página principal