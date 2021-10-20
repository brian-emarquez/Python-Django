from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.
def home(request):
    # texto plano , mala practica
    blogs = Post.objects.all()
    return render(request, "blog/home.html", {'blogs':blogs})

def blog(request, id):
    # texto plano , mala practica
    blog = Post.objects.get(id=id)
    return render(request, "blog/blog.html", {'blog':blog})