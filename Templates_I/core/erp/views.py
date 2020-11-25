from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def myfirstView(request):
    return HttpResponse('Hola esto es mi primero URL')