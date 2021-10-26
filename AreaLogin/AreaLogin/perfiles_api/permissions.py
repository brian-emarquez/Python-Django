"""Permiso personalisado"""
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Perimite usuario editar su propio perfil"""
    
    
    def has_object_permission(self, request, view, obj):
        """Chequear si un usuario esta intentando editar su propio perfil """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
    
    