from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class PublicadosManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLICADO)

class Post(models.Model):

    class Status(models.TextChoices):
        RASCUNHO = 'RSC', 'Rascunho'
        PUBLICADO = 'PUB', 'Publicado'

    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publicado')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    corpo = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateField(auto_now_add=True)
    # ^^^ By using auto_now_add, the date will be saved automatically when CREATING an object
    modificado = models.DateTimeField(auto_now=True)
    # ^^^ By using auto_now, the date will be updated automatically when SAVING an object an object.
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.RASCUNHO)
    objetos = models.Manager()
    publicacoes = PublicadosManager()


    class Meta:
        ordering = ['-publicado']
        indexes = [
            models.Index(fields=['-publicado'])
        ]

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('blog:detalhe_do_post', args=[self.publicado.year,
                                                     self.publicado.month,
                                                     self.publicado.day,
                                                     self.slug])