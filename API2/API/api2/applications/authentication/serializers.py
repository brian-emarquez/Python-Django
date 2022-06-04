
from dataclasses import fields
from os import access
from .models import Roles, Users, Permissions, PermissionsRoles
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
    
    
class PermissionsRolesSerializer(serializers.ModelSerializer):
    
    pk = serializers.IntegerField(source='Permission.pk')
    Name = serializers.CharField(source='Permission.Name')

    class Meta:
        model = PermissionsRoles
        fields = [
            'pk',
            'Name',
            'Read',
            'Update',
            'Delete',
            'Create',
            'Active'
        ]
  
class RolesDetailSerializer(serializers.ModelSerializer):
    
    Permissions = PermissionsRolesSerializer(
        many=True, 
        source='RolePermissionRoles'
        )
    
    class Meta:
        model = Roles
        fields = [
            'pk',
            'Name',
            'Description',
            'Active',
            'Permissions'
        ]
class UsersDetailSerializer(serializers.ModelSerializer):

    Username = serializers.CharField(required=False, source='username')
    Name = serializers.CharField(required=False, source='first_name')
    LastName = serializers.CharField(required=False, source='last_name')
    Email = serializers.CharField(required=False, source='email')
    Roles = RolesDetailSerializer(many=True)

    class Meta:
        model = Users
        fields = [
            'pk',
            'Username',
            'Email',
            'Name',
            'LastName',
            'Roles'
        ] 
    
# Se hereda de miosmo jwt (USERNAME, PASSWORD)
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def create(self, validated_data):
        pass
    
    def update(self, instance, validated_data):
        pass
    
    def validate(self, attrs):
        # Sobre Escri
        #print("attrs-->", attrs)
        data = super().validate(attrs)
        # print("---> data ", data)
        #print("self--<", self)
        #print("selfUser--<", self.user)
        refresh = self.get_token(self.user)
        print("refresh--<", refresh)
        
        data['refresh'] = str(refresh)
        #print("--",refresh.access_token)
        data['access'] = str(refresh.access_token)
        #print("data ---->",data)
                  
        try:
            #Creamos campo User en el dic
            instance = Users.objects.get(pk=self.user.pk)
            data['user'] = UsersDetailSerializer(instance).data
            print("ata['user']--->", data['user'])
            
        except Exception as e:
            print("Error--->", e)
            data['user'] = UserSerializer(self.user).data
            #data['user']['Roles'] = []
        return data
            
    @classmethod
    def get_token(cls, user):
        #print(user)
        tok = super().get_token(user)
        #print("tok--->", tok)
        return tok

class UserSerializer(serializers.ModelSerializer):
    
    """
    Class to serialize Users model
    """
    Username = serializers.CharField(required=False, source='username')
    Name = serializers.CharField(required=False, source='first_name')
    LastName = serializers.CharField(required=False, source='last_name')
    Email = serializers.CharField(required=False, source='email')

    class Meta:
        model = User
        fields = [
            'pk',
            'Username',
            'Email',
            'Name',
            'LastName',
        ]
