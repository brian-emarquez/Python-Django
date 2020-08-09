# Plantillas III
# Estructuras de control de flujo

from django.http import HttpResponse
import datetime
from django.template import Template, Context


class Persona(object):

    # Constructor
    def __init__(self, nombre, apellido): 
        self.nombre=nombre
        self.apellido=apellido

def saludo (request): # primera vista

    p1 = Persona("Brian", "Marquez")

    temasDelCurso = ["Plantillas", "Modelos", "Formularios", "Vistas", "despliegue"]
    #temasDelCurso = []

    ahora=datetime.datetime.now()

    doc_externo = open("C:/Users/brian/Documents/Python-Django/PlantillasIV/template/myTemplate.html")
    plt = Template(doc_externo.read())
    
    doc_externo.close()

    ctx=Context({"nombre_persona":p1.nombre, "apellido_persona": p1.apellido, "momento_actual": ahora, "temas":temasDelCurso}) #Diccionario donde se guadar los nombres

    documento=plt.render(ctx)

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





