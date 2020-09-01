from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50, verbose_name="La direccion") # Personalisa como se vera el Mensage
    email=models.EmailField(blank=True, null=True) # campo no requerido
    tfno=models.CharField(max_length=7)

    # Show names
    def __str__(self):
        return self.nombre # mostar el nombre en el panel


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