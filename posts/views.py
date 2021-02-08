from django.shortcuts import render
#Classe que vai ser herdada para criar a classe do view
from django.views.generic.list import ListView
#Classe que vai ser herdada para criar detalhes dentro do post
from django.views.generic.edit import UpdateView
from posts.models import Post


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 10
    context_object_name = 'posts'

class PostBusca(PostIndex):
    pass


class PostCategoria(PostIndex):
    pass


class PostDetalhes(UpdateView):
    pass








