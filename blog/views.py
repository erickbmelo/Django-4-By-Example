from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Post


# Create your views here.
def lista_de_posts(request):
    lista_posts = Post.publicacoes.all()
    # Paginação com 3 posts por página
    paginator = Paginator(lista_posts, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # Se o número da página não for um inteiro, devolve a primeira
        posts = paginator.page(1)
    except EmptyPage:
        # Se for requisitada uma página maior que o range, devolve a última
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/lista.html', {'posts': posts})

def detalhe_do_post(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLICADO,
                             slug=post,
                             publicado__year=year,
                             publicado__month=month,
                             publicado__day=day)
    return render(request, 'blog/post/detalhe.html', {'post': post})

class PostListView(ListView):
 """
 Alternative post list view
 """
 queryset = Post.publicacoes.all()
 context_object_name = 'posts'
 paginate_by = 3
 template_name = 'blog/post/lista.html'
