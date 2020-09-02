from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# vistas
def busqueda_productos(request):

    return render(request, "busqueda_productos.html")

def buscar(request):

    mensaje="Articulos buscado: %r" %request.GET["prd"]
    return HttpResponse(mensaje)