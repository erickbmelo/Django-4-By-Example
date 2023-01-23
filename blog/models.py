from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    corpo = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateField(auto_now_add=True)
    # ^^^ By using auto_now_add, the date will be saved automatically when CREATING an object
    modificado = models.DateTimeField(auto_now=True)
    # ^^^ By using auto_now, the date will be updated automatically when SAVING an object an object.

    class Meta:
        ordering = ['-publicado']
        indexes = [
            models.Index(fields=['-publicado'])
        ]

    def __str__(self):
        return self.titulo