from django.shortcuts import render
from .models import Post


def showblog(request):
    blogs = Post.objects
    return render(request, 'blog/blog.html', {'blogs': blogs})
