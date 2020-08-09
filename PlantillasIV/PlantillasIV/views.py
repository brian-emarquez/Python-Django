# Plantillas IV
# Condicionales, filtros y cargadores de plantillas
# Filosifia de django sueprar la parte logica del diseño
# https://docs.djangoproject.com/en/3.1/ref/templates/builtins/

from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader

class Persona(object):

    # Constructor
    def __init__(self, nombre, apellido): 
        self.nombre=nombre
        self.apellido=apellido

def saludo (request): # primera vista

    p1 = Persona("Brian", "Marquez")

    temasDelCurso = ["Plantillas", "Modelos", "Formularios", "Vistas", "despliegue"]
    ahora=datetime.datetime.now()

    # CARGADORES DE PLANTILLA
    #doc_externo = open("C:/Users/brian/Documents/Python-Django/PlantillasIV/template/myTemplate.html")
    #plt = Template(doc_externo.read())
    #doc_externo.close()

    doc_externo = loader.get_template('myTemplate.html')

    documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona": p1.apellido, "momento_actual": ahora, "temas":temasDelCurso}) 
    return HttpResponse(documento)

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





