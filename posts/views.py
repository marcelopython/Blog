from django.shortcuts import render
#Classe que vai ser herdada para criar a classe do view
from django.views.generic.list import ListView
#Classe que vai ser herdada para criar detalhes dentro do post
from django.views.generic.edit import UpdateView


class PostIndex(ListView):
    pass


class PostBusca(PostIndex):
    pass


class PostCategoria(PostIndex):
    pass


class PostDetalhes(UpdateView):
    pass








