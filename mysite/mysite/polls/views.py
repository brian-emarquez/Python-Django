from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hola esta es una pagina en blanco de Django.")