from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from core.erp.models import Category, Product

# Create your views here.
def myfirstView(request):

    data ={
        'name': 'brian',
        'categories': Category.objects.all()

    }
    return render(request, 'index.html', data)

def mysecondView(request):

    data = {
        'name': 'brian',
        'products': Product.objects.all()

    }
    return render(request, 'second.html', data)

