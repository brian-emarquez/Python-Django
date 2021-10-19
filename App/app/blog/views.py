from django.shortcuts import render, HttpResponse

# Create your views here.
def blog(request):
    return HttpResponse("Hola esta en app de blog")