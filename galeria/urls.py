from django.urls import path
from galeria.views import index,imagem

urlpatterns = [
    path('', index, name='index'), #este index esta retornando o HTTP response. Essas aspas  esta se referindo a rota principal, não possui nenhum direcionamento.  
    path('imagem/', imagem, name ='imagem'),
]