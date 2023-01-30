from django.shortcuts import get_object_or_404, render

from .models import Post


# Create your views here.
def lista_de_posts(request):
    posts = Post.publicacoes.all()
    return render(request, 'blog/post/lista.html', {'posts': posts})

def detalhe_do_post(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLICADO,
                             slug=post,
                             publicado__year=year,
                             publicado__month=month,
                             publicado__day=day)
    return render(request, 'blog/post/detalhe.html', {'post': post})