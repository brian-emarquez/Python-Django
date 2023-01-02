from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.core.cache import cache
from .models import *

def home(request):
    payload = []
    db = None
    if cache.get('fruits'):
        payload = cache.get('fruits')
        db = 'estas en redis :)'
        print(cache.ttl("fruits"))
    else:
        objs = Fruits.objects.all()
        for obj in objs:
            payload.append(obj.fruit_name)
        db = 'estas en postgres :O' 

        cache.set('fruits', payload, timeout=10)

    return JsonResponse({'status': 200, 'db': db, 'data': payload})