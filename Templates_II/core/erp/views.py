from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

# Create your views here.
def myfirstView(request):

    data ={
        'name':'brian'
    }
    return render(request, 'index.html', data)