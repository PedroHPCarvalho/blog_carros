# ARQUIVO FORM 
# - tem como objetivo definir os modelos de formularios da aplicação pelo 
# django, neste caso foi utilizado o ModelForm, que cria um formulario 
# a partir do modelo do banco de dados, sendo assim facilita integrar
# os dados ao banco de dados
from django import forms
from .models import Post


# Classe PostForm cria um formulario a partir do modelo Post


class PostForm(forms.ModelForm):
    class Meta:
        # aqui definimos o modelo base para o formulario e quais campos do 
        # modelo usaremos 
        model = Post
        fields = ['title', 'body']