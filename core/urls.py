from django.urls import path
from .views import index, principal, contato

# Abaixo configure todas as rotas de urls, não utilizar o arquivo urls.py que fica dentro da aplicação CORE
urlpatterns = [
    path('', index, name='index'),
    path('principal/', principal, name='principal'),
    path('contato/', contato, name='contato'),
]