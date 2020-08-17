from django.db import models

# Create your models here.

# Create Table
# Insertar Registros
# Actualizar Registros  
# Borrar Registros
class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    tfno=models.CharField(max_length=7)


class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.ImageField()


class Pedidos(models.Model):
    nombre=models.ImageField()
    fecha=models.DateField()
    entregado=models.BooleanField()
