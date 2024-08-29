from django.db import models

# Aqui ficarão os códigos responsáveis por ajustar o banco de dados da aplicação.
 
class Base(models.Model):
    campo0 = models.CharField('Nome', max_length=255)
    campo1 = models.CharField('Estado', max_length=255)
    campo2 = models.CharField('País', max_length=255)
    criado = models.DateField('Data de Criação', auto_now_add=True)
    
    class Meta:
        abstract = False
