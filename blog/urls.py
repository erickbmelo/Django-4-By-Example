from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.lista_de_posts, name='lista_de_posts'),
    path('<int:id>/', views.detalhe_do_post, name='detalhe_do_post')
]