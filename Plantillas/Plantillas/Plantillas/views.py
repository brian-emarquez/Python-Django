# Plantillas I

from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo (request): # primera vista

    #Template
    doc_externo=open("C:/Users/brian/Documents/Python-Django/Plantillas/template/myTemplate.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
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
    
    #edadActual=18 

    periodo = agno-2020
    edadFutura = edad+periodo
    documento="<html><body><h2>En el año %s tendras %s años" %(agno, edadFutura)

    return HttpResponse(documento)





