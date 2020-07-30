from django.http import HttpResponse

# Primera Vista
def saludo (request):
    return HttpResponse("Hola Github esta es nuestra primera pagina con django")