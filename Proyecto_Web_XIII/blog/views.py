from django.shortcuts import render
from blog.models import Post


# Create your views here.

def blog(request):
    
    posts=Post.objects.all()
    return render(request, "blog/blog.html",  {"posts":posts})

