from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade): # Define a função 'hello' que recebe um parâmetro 'request' e dois parâmetros 'nome' e 'idade'
    return HttpResponse('<h1>Hello {}, você tem {} anos de idade</h1>'.format(nome, idade)) # Retorna uma resposta HTTP com o texto 'Hello <nome>' no corpo da resposta