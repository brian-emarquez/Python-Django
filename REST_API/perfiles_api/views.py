#from django.shortcuts import render
from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloapiView(APIView):
    """Api view de prueba"""
    
    def get(self, request, format=None):
        """retornar lista de caracteristicas de APIVIEW"""
        
        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, patch, put delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la logicade nusetra aplicacion',
            'Esta mapeado manualmente a los URLS',   
        ]
        
        return Response({'message':'Hello', 'an_apiview': an_apiview})

