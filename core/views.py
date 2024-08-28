from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def principal(request):
    return render(request, 'principal.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('principal')  # Uma vez logado com sucesso, redireciona para a página principal
        else:
            return render(request, 'index.html', {'error': 'Credenciais inválidas'})
        
    return render(request, 'index.html')

@login_required
def principal_view(request):
    return render(request, 'principal.html')
