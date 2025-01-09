from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import PostForm
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


def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog/')
    else:
        form = PostForm()
    return render(request, 'blog/new_post.html', {'form': form})


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("/blog/")
    else:
        form = PostForm(instance=post)
    return render(request, "blog/edit_post.html", {"form": form, "post": post})


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect("/blog/")
    return render(request, "blog/delete_post.html", {"post": post})
            