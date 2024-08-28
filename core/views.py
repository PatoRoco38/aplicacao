from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def principal(request):
    return render(request, 'principal.html')

def contato(request):
    return render(request, 'contato.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('principal')  # Uma vez logado com sucesso, redireciona para a página principal
        else:
            return HttpResponse("A tentativa de login falhou, verifique os dados digitados e tente novamente.")
        
    return render(request, 'index.html')
