from dataclasses import field
from django.contrib.auth.models import User, Group
from rest_framework import serializers

#https://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = User
        fields = ['url','username', 'email', 'groups']
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']