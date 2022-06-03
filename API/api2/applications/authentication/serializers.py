
from dataclasses import fields
from .models import Roles, Users, Permissions, PermissionsRoles
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
    
# se hereda de miosmo jwt (USERNAME, PASSWORD)
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def create(self, validated_data):
        pass
    
    def update(self, instance, validated_data):
        pass
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data
        
        # print("-> data ", data)
        # refresh = self.get_token(self.user)
        # print("-> refresh  ", refresh)
        
        try:
            pass
        except Exception as e:
            pass
        return data
        
        
        
    @classmethod
    def get_token(cls, user):
        tok = super().get_token(user)
        return tok

        
    
    