
from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "projectoWebApp/home.html")

def servicios(request):
    return render(request, "projectoWebApp/servicios.html")

def tienda(request):
    return render(request, "projectoWebApp/tienda.html")

def blog(request):
    return render(request, "projectoWebApp/blog.html")

def contacto(request):
    return render(request, "projectoWebApp/contacto.html")

