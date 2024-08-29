import csv
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import FileSystemStorage
from .models import Base

def index(request):
    return render(request, 'index.html')

def principal(request):
    return render(request, 'principal.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('principal')  # Uma vez logado com sucesso, redireciona para a página principal
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'index.html', {'form_login': form_login})

@login_required
def principal_view(request):
    return render(request, 'principal.html')

@login_required
def principal_view(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            return render(request, 'principal.html', {'error': 'Este arquivo não é válido'})
        
        arquivo = FileSystemStorage()
        filename = arquivo.save(csv_file.name, csv_file)
        uploaded_file_url = arquivo.url(filename)

        try:
            with open(arquivo.path(filename), newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >=3:
                        # Ordem dos campos a serem inclusos no banco
                        Base.objects.create(campo0=row[1], campo1=row[2], campo2=row[3])
        except UnicodeDecodeError:
            try:
                with open(arquivo.path(filename), newline='', encoding='ISO-8859-1') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if len(row) >=3:
                            Base.objects.create(campo0=row[1], campo1=row[2], campo2=row[3])
                        else:
                            print(f'Planilha com {row} colunas')
            except Exception as e:
                print(f'Erro ao processar arquivo: {e}')
                # return render(request, 'principal.html', {'Erro': f'Erro ao tentar o upload do arquivo: {str(e)}'})

        return render(request, 'principal.html', {'Sucesso!': 'Arquivo carregado com sucesso!'})
    
    return render(request, 'principal.html')