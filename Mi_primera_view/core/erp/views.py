from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def myfirtsView(request):

    data = {
        'name' : 'brian'
    }
    return JsonResponse(data)
    #return HttpResponse("Hola esta es mi primera URL")