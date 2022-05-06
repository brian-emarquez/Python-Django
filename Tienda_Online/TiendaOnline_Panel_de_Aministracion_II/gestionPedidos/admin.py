from django.contrib import admin

from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class clientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "tfno") # Monstar las columnas de los atributos
    search_fields=("nombre", "tfno") # Barra de busqueda

admin.site.register(Clientes, clientesAdmin) # llamado a la funcion
admin.site.register(Articulos)
admin.site.register(Pedidos)
