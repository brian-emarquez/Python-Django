from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    tfno=models.CharField(max_length=7)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()
    
    def __str__(self): # visualizar los elemtnos de la base de datos
        return 'el nombres es %s la se seccion es %s y el precio es %s' % (self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    nombre=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()

# SHELL

# Articulos.objects.filter(seccion='decoracion', nombre='lampara')
# Articulos.objects.filter(seccion='decoracion', nombre='mesa')  mayor 
# Articulos.objects.filter(seccion='deportes', precio__lte=100) menor