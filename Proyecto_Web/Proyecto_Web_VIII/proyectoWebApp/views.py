from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "proyectoWebApp/home.html")

def servicios(request):
    return render(request, "proyectoWebApp/servicios.html")

def tienda(request):
    return render(request, "proyectoWebApp/tienda.html")

def blog(request):
    return render(request, "proyectoWebApp/blog.html")

def contacto(request):
    return render(request, "proyectoWebApp/contacto.html")