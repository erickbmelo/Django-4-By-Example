from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    # path('', views.lista_de_posts, name='lista_de_posts'),
    path('', views.PostListView.as_view(), name='lista_de_posts'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.detalhe_do_post, name='detalhe_do_post'),
    path('<int:post_id>/compartilha_post/', views.compartilha_post, name='compartilha_post')
]
