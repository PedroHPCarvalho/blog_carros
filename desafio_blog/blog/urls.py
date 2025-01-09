# URLS
# tem como objetivo mapear as urls para as views correspondentes,
# conectando as URLS com as funções que as tratam respectivamente

from django.urls import path
from . import views

# pratica importante para organizar e diferenciar as URLs entre 
# diferentes os apps, o uso do app_name ajuda a evitar os conflitos 
# de nomes de URLs
app_name = "blog"

# urlpatterns é uma lista com os mapeamentos entre URLs e views
urlpatterns = [
    # o uso do name é usado para identificar as rotas de forma simples e de 
    # facil reutilização nos templetes e em outras partes do codigo
    path('', views.index, name="index"),
    path("<int:post_id>", views.detailed_post, name="detailed_post"),
    path("new_post", views.new_post, name="new_post"),
    path("<int:post_id>/edit/", views.edit_post, name="edit_post"),
    path("<int:post_id>/delete/", views.delete_post, name="delete_post"),
]