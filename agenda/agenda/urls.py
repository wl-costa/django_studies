"""
URL configuration for agenda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('agenda/evento/', views.evento), 
    path('agenda/evento/submit', views.submit_evento), # URL para submeter um evento
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento), # URL para deletar um evento
    path('', RedirectView.as_view(url='/agenda/')), # Redireciona para a página agenda.html caso a URL seja vazia
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('agenda/filter/', views.filter_eventos),
    path('agenda/search/', views.search_eventos),
]

urlpatterns += [
    path('auth/', include('social_django.urls', namespace='social')),
]
