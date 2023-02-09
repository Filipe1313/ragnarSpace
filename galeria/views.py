from django.shortcuts import render


def index(request): # Index é o caminho default.
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')