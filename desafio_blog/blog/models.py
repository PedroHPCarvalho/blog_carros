# MODELS
# - serve de GUIA para a criação do banco de dados, utilizada juntamente com
# as migrations para manter o banco de dados da aplicação atualizado de acordo
# com a estrutura atual da aplicação

from django.db import models

# Create your models here.

# Clase Post sendo o modelo de tabela que sera criado no
# banco para armazenar as informações


class Post(models.Model):
    # Campos do modelo, informações relevantes a serem salvas no banco
    # imagem da postagem
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    # titulo do post
    title = models.CharField(max_length=60)
    # subtitulo do post
    subtitle = models.CharField(max_length=150)
    # corpo do post
    body = models.TextField()
    # data de criação do post
    created_at = models.DateTimeField(auto_now_add=True)
