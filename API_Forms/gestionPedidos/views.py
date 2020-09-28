from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

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

# Creacion de formulario de contacto - Manera Manual
'''
def contacto(request):

    if request.method=="POST": # si el envia informacion

        subject = request.POST["asunto"]
        message=request.POST["mensaje"] + " " + request.POST["email"] 
        email_from=settings.EMAIL_HOST_USER
        recipient_list = ["registropsicoune@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
        return render(request, "gracias.html")
        
    return render(request, "contacto.html")
'''
# Creacion de formulario de contacto - Uusando Api Form

def contacto(request):

    if request.method=="POST": # si el envia informacion

        miformulario= FormularioContacto(request.POST)
        
        if miformulario.is_valid():
            intform = miformulario.cleaned_data

            send_mail(intform['asunto'], intform['mensaje'], intform.get('email',''),['test0update0data@gmail.com'])

            return render(request, "gracias.html")
    else:

        miformulario = FormularioContacto()
    return render(request, "formulario_contacto.html", {"form":miformulario})