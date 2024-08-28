from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def principal(request):
    return render(request, 'principal.html')

def contato(request):
    return render(request, 'contato.html')
