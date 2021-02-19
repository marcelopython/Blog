from django.shortcuts import render, redirect
#Classe que vai ser herdada para criar a classe do view
from django.views.generic.list import ListView
#Classe que vai ser herdada para criar detalhes dentro do post
from django.views.generic.edit import UpdateView
from posts.models import Post
from django.db.models import Q, Count, Case, When
from comentarios.forms import FormComentario
from comentarios.models import Comentario
from django.contrib import messages

class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(publicado_post=True)
        qs = qs.annotate(
            numero_comentarios = Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )
        return qs


class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')
        if not termo:
            return qs

        qs = qs.filter(
            Q(titulo_post__icontains=termo) |
            Q(autor_post__first_name__iexact=termo) |
            Q(conteudo_post__iexact=termo) |
            Q(excerto_post__icontains=termo) |
            Q(categoria_post__nome_cat__iexact=termo)
        )
        return qs

class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'

    def get_queryset(self):
        qs = super().get_queryset()

        categoria = self.kwargs.get('categoria', None)
        if not categoria:
            return qs
                        #Busca o nome da categoria atravez da fk
                        # __iexact busca exata o (i) quer dizer que e Case-insensitive
        qs = qs.filter(categoria_post__nome_cat__iexact=categoria)
        return qs


class PostDetalhes(UpdateView):
    template_name = 'posts/post_detalhes.html'
    model = Post
    form_class = FormComentario
    context_object_name = 'post'

    def form_valid(self, form):
        post = self.get_object()
        comentario = Comentario(**form.cleaned_data)
        comentario.post_comentario = post

        if self.request.user.is_authenticated:
            comentario.usuario_comentario = self.request.user

        comentario.save()
        messages.success(self.request, 'Comentário enviado com sucesso')
        return redirect('post_detalhes', pk=post.id)



