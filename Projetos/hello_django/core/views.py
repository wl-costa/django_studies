from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome):
    return HttpResponse('<h1><center>Hello {}</center></h1>',format(nome)) # Retorna uma resposta HTTP com o texto 'Hello <nome>' no corpo da resposta