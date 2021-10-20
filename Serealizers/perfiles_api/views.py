#from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured
from django.http import response
import rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# se importa el serializer dentro de la App
from perfiles_api import serializers

class HelloapiView(APIView):
    """Api view de prueba"""
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """retornar lista de caracteristicas de APIVIEW"""
        
        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, patch, put delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la logicade nusetra aplicacion',
            'Esta mapeado manualmente a los URLS',   
        ]
        
        return Response({'message':'Hello', 'an_apiview': an_apiview})
    
    def post(self, request):
        """ Crea un mensaje con nuestro nombre """
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response ({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def put(self, request, pk=None):
        """ Maneja actualizar un objetoo """
               
        return Response ({'method':'PUT'})
    
    def patch(self, request, pk=None): 
        """ Maneja actualizacion parcial de un objeto """
        
        return Response ({'method':'PATCH'})
    
    
    def put(self, request, pk=None): 
        """ Maneja actualizacion parcial de un objeto """
        
        return Response ({'method':'PUT'})
    
    def delete (self, request, pk=None): 
        """ Borrar un Objeto """
        
        return Response ({'method':'DELETE'})
    




            
