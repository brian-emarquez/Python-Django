from django.db import models

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
