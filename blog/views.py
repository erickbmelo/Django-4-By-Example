from django.shortcuts import get_object_or_404, render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def lista_de_posts(request):
    lista_posts = Post.publicacoes.all()
    # Paginação com 3 posts por página
    paginator = Paginator(lista_posts, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    return render(request, 'blog/post/lista.html', {'posts': posts})

def detalhe_do_post(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLICADO,
                             slug=post,
                             publicado__year=year,
                             publicado__month=month,
                             publicado__day=day)
    return render(request, 'blog/post/detalhe.html', {'post': post})