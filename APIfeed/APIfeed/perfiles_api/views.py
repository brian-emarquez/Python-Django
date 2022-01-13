# from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.utils.translation import to_language
from rest_framework import authentication, permissions
import rest_framework
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# token Authntication
from rest_framework.authentication import TokenAuthentication

# Area de loggin
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# se importa el serializer dentro de la App
from perfiles_api import serializers, models, permissions


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

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ Crea un mensaje con nuestro nombre """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Maneja actualizar un objetoo """

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Maneja actualizacion parcial de un objeto """

        return Response({'method': 'PATCH'})

    def put(self, request, pk=None):
        """ Maneja actualizacion parcial de un objeto """

        return Response({'method': 'PUT'})

    def delete(self, request, pk=None):
        """ Borrar un Objeto """

        return Response({'method': 'DELETE'})

# Viewset


class HelloViewSet(viewsets.ViewSet):
    """ Test API viewset """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Retornas mensae de hola munfo"""

        a_viewsets = [
            'usando 2 acciones (list, create, retrieve, update, partial update',
            'mapea a los upts usando routers',
            'mas funcionalidad con menos codigo',
        ]

        return Response({'message': 'Hola!', 'a_viewsets': a_viewsets})

    def create(self, request):
        """Retornas mensaje de hola mundo"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Optiene el objeto y su ID, ejecurtamos el metodo GET"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Actualiza un objeto"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Actualiza  parcialmente un objeto"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Destruye un objeto"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """crear y actualizar perfiles"""
    serializer_class = serializers.UserPerfilSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)  # tupla
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Crea tokens de authentication de usuario"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewsSet(viewsets.ModelViewSet):
    """Maneja el crear, leer y actualizar el profile feeed """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        """ Setear el perfil de usuaio para el usuario que esta logeado """
        serializer.save(user_profile=self.request.user)
    
    
    
    