from pyexpat import model
from django.db import models

from application.modelRelacion.models import Person


class Vehiculo(models.Model):
    """
    Esto es una pruebal de modelos
    """
    
    Marca = models.CharField(
        max_length=150,
    )
    
    Llantas = models.DecimalField(
            max_digits=20,
            decimal_places=8,
            default=0.0,
            help_text='esto es son llantas'
    )
    
    Puertas = models.DecimalField(
            max_digits=20,
            decimal_places=8,
            default=0.0,
            help_text='esto son puertas'
    )
    
    Fechacompra = models.DateTimeField(
        auto_now_add=True
    )
    
class Encargado(models.Model):
    user = models.CharField(max_length=128)
    #user = models.ManyToManyField(Person)
    Person = models.ForeignKey(Person, on_delete=models.CASCADE)
                        
    def __str__(self):
        return self.name


