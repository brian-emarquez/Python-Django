from email.policy import HTTP
from urllib import response
from django.shortcuts import render
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from .serializers import MyTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_401_UNAUTHORIZED,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_204_NO_CONTENT)
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    # Serializador
    # es usado cuando es llamado el metodo POST
    serializer_class = MyTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        # si existe devuelve el numbre sino "NONE"
        user = authenticate(
            username = username,
            password = password                    
        )   
        
        # print(type(user))
        # print(user)
                
        if user:
            print(" si existe el usuario")
            # Usamos el Serializers
            requestSerializer = self.serializer_class(data=request.data)
            
            # llamamos al serializador
            if requestSerializer.is_valid():
                # usarndo el validad de serializers
                dataResponse = requestSerializer.validated_data
                #print("....si es valido", dataResponse)
                
                
                dataResponse = requestSerializer.validated_data
                
                if User.objects.get(pk=dataResponse['user']['pk']).is_staff:
                    return Response(data=dataResponse, status=HTTP_200_OK)
                
                else:
                    return Response(data={'unauthorized user'},
                                status=HTTP_401_UNAUTHORIZED)
            else:
                return Response(data='Malas credenciasles',
                                Status=HTTP_400_BAD_REQUEST)                     
        else:
            return Response(
                # Muestr a en pantalla de views
                data ="No existe",
                status = HTTP_400_BAD_REQUEST,
            )
