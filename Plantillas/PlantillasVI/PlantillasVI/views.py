# Plantillas VI
# Herencia de plantillas


from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

class Persona(object):

    # Constructor
    def __init__(self, nombre, apellido): 
        self.nombre=nombre
        self.apellido=apellido

def saludo (request): # primera vista

    p1 = Persona("Brian", "Marquez")

    temasDelCurso = ["Plantillas", "Modelos", "Formularios", "Vistas", "despliegue"]
    ahora=datetime.datetime.now()

    return render(request, "myTemplate.html",{"nombre_persona":p1.nombre, "apellido_persona": p1.apellido, "momento_actual": ahora, "temas":temasDelCurso})

def despedida (request):
    return HttpResponse("Hasta luego Github")

# Funcion que muestra la fecha Actual
def dameFecha(request):

    fecha_actual=datetime.datetime.now()

    documento = """
    <html>
    <body>
    <h2>

    Fecha y Hora Actuales: %s

    </h2>
    </boddy>
    </html>""" % fecha_actual

    return HttpResponse(documento)

# Funcion que calcula la edad en fecha indeterminadas
def calculaEdad(request, agno, edad):
    
    periodo = agno-2020
    edadFutura = edad+periodo
    documento="<html><body><h2>En el año %s tendras %s años" %(agno, edadFutura)

    return HttpResponse(documento)


def cursoC(request):

    fecha_actual=datetime.datetime.now()
    return render(request, "CursoC.html",{"dameFecha":fecha_actual})

def cursoCss(request):

    fecha_actual=datetime.datetime.now()
    return render(request, "CursoCss.html",{"dameFecha":fecha_actual})


