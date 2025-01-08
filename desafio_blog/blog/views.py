from django.shortcuts import render
from django.http import Http404
from .models import Post

# Create your views here.
 

def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts}) 


def detailed_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post não encontrado")
    return render(request, "blog/detailed_post.html", {"post": post})