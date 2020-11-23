from ORM_II.wsgi import *# importamos lo modulos de la carpeta wsgi.py

from core.erp.models import Type

# LISTAR

# EJECUTAR FILTROS - AYUDA EN LA BUSQUEDA - LIKE SQL
# obj = Type.objects.filter(name__contains='pre') #BUusca la palabrs que empiesa a Pre
obj = Type.objects.filter(name__endswith='a') #Busca la palabra que termina con a

print(obj)

# Ver el SQL DE LA CONSULTA
obj1 = Type.objects.filter(name__contains='terry').query
print(obj1)

# Excluir
obj2= Type.objects.filter(name__icontains='a').exclude(id=5) # no toma el cuenta el numero 5
print(obj2)

# Interando
# Excluir
for i in Type.objects.filter(name__icontains='a').exclude(id=5): # no toma el cuenta el numero 5
    print(i.name)