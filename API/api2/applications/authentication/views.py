from email.policy import HTTP
from urllib import response
from django.shortcuts import render
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from .serializers import MyTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST)
from django.contrib.auth import authenticate

# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    # Serializador
    serializer_class = MyTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(
            username = username,
            password = password                    
        )   
        
    
        print(type(user))
        print(user)
                
        if user:
            print(" si existe el usuario")
            # Usamos el Serializers
            requestSerializer = self.serializer_class(data=request.data)
            print("::::::")
            
            if requestSerializer.is_valid():
                # usarndo el validad de serializers
                print("*******")
                dataResponse = requestSerializer.validated_data
                print("....si es valido", dataResponse)
            
            
            
        else:
            return Response(
                data ="No existe",
                status = HTTP_400_BAD_REQUEST,
            )
            
        
        #print("esto es el post", request.data)
        return Response(data="holaa", status=HTTP_200_OK)