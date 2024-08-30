from django.urls import path, include
from .views import *

# Abaixo configure todas as rotas de urls, não utilizar o arquivo urls.py que fica dentro da aplicação CORE
urlpatterns = [
    path('', login_view, name='login_view'),
    path('principal/', principal_view, name='principal'),
    path('dados/', dados_view, name='dados'),
]