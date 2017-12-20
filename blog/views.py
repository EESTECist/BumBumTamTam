from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category
from .forms import PostForm

def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        form.save()
    form = PostForm()
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, "index.html", context={"posts": posts, "categories": categories, "form": form})

def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "post.html", context={"post": post})

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request, "category.html", context={"category": category})
