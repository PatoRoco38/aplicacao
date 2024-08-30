from django.db import models

# Aqui ficarão os códigos responsáveis por ajustar o banco de dados da aplicação.
 
class Base(models.Model):
    campo1 = models.CharField('Console', max_length=255)
    campo2 = models.CharField('Jogo', max_length=255)
    
    class Meta:
        abstract = False
