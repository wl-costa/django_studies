from django.db import models

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True) # A descrição pode ser nulo ou vazio
    data_evento = models.DateTimeField(verbose_name='Data do Evento') # A data do evento é obrigatória
    data_criacao = models.DateTimeField(auto_now=True) # A data de criação do evento é automatica

    class Meta:
        db_table = 'evento' # Define o nome da tabela no banco de dados como 'evento' ao invés de 'core_evento' que é o padrão do Django
        
    def __str__(self):
        return self.titulo # Retorna o título do evento como representação do objeto
    