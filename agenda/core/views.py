from django.shortcuts import render, redirect # Importa as funções render e redirect do módulo shortcuts
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# def index(request):
#     return redirect('/agenda/') # Redireciona para a página agenda.html

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='/login/') # Verifica se o usuário está logado, caso não esteja, redireciona para a página de login
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario) # Filtra os eventos do usuário logado e armazena na variável evento
    dados = {'eventos': evento} # Cria um dicionário com o evento e armazena na variável dados
    return render(request, 'agenda.html', dados) # Renderiza a página agenda.html com os dados do dicionário