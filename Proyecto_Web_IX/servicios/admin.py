from django.contrib import admin
from .models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=("created", "update")

admin.site.register(Servicio, ServicioAdmin)