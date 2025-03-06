from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True) # A descrição pode ser nulo ou vazio
    data_evento = models.DateTimeField(verbose_name='Data do Evento') # A data do evento é obrigatória, o verbose_name é o nome que será exibido no formulário
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data da Criação') # A data de criação do evento é automatica
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # Se o usuário dono do evento for excluido da aplicação, todos os eventos serão excluídos

    class Meta:
        db_table = 'evento' # Define o nome da tabela no banco de dados como 'evento' ao invés de 'core_evento' que é o padrão do Django
        
    def __str__(self):
        return self.titulo # Retorna o título do evento como representação do objeto
    
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y às %H:%M Hs')