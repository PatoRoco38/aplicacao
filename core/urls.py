from django.urls import path, include
from django.contrib import admin
from .views import *

# Abaixo configure todas as rotas de urls, não utilizar o arquivo urls.py que fica dentro da aplicação CORE
urlpatterns = [
    path('', index, name='index'),
    path('login_view', login_view, name='login_view'),
    path('principal/', principal, name='principal'),
]