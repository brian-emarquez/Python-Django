from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class clientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "tfno") # Monstar las columnas de los atributos
    search_fields=("nombre", "tfno") # Barra de busqueda

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion", ) # muestras la secciones

class PedidosAdmin(admin.ModelAdmin):
    list_display=("nombre", "fecha") #mostar
    list_filter=("fecha", )  # filtro
    date_hierarchy="fecha" # linea de datos historicos

admin.site.register(Clientes, clientesAdmin) # llamado a la funcion
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)