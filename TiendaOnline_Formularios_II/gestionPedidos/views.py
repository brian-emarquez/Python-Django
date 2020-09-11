from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# vistas
def busqueda_productos(request):

    return render(request, "busqueda_productos.html")

def buscar(request):

    if request.GET["prd"]:
        #mensaje="Articulos buscado: %r" %request.GET["prd"]
        producto = request.GET["prd"]

        articulos=articulos.objects.filter(nombre__icontains=producto)# consultar con la base de datos

        return render(request, "resultado_busqueda.html", {"articulos": articulos, "query":producto})
        
    else:
        mensaje="NO HAS INTRODUCIDO NADA"

    return HttpResponse(mensaje)