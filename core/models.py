from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify

# Aqui ficarão os códigos responsáveis por ajustar o banco de dados da aplicação.
 
class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    
    class Meta:
        abstract = True
