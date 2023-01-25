from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def lista_de_posts(request):
    posts = Post.publicacoes.all()
    return render(request, 'lista.html', {'posts': posts})

def detalhe_do_post(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLICADO)
    return render(request, 'detalhe.html', {'post': post})