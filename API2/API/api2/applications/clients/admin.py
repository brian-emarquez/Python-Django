from django.contrib import admin

from .models import Clientes, Addresses


# Register your models here.
admin.site.register(Clientes)
admin.site.register(Addresses)

