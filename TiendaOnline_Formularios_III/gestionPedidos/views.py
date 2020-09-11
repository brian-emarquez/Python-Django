from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.
# vistas
def busqueda_productos(request):

    return render(request, "busqueda_productos.html")

def buscar(request):

    if request.GET["prd"]:
        #mensaje="Articulos buscado: %r" %request.GET["prd"]
        producto = request.GET["prd"]

        # Limitar Nª de caracteres a buscar BBDD
        if len(producto)>20:
            mensaje = "Texto de busqueda demasiado largo"
        else:
            articulos=Articulos.objects.filter(nombre__icontains=producto)# consultar con la base de datos
            return render(request, "resultado_busqueda.html", {"articulos": articulos, "query":producto})
        
    else:
        mensaje="NO HAS INTRODUCIDO NADA"

    return HttpResponse(mensaje)

# Creacion de formulario de contacto 1
def contacto(request):

    if request.method=="POST": # si el envia informacion
        return render(request, "gracias.html")
        
    return render(request, "contacto.html")