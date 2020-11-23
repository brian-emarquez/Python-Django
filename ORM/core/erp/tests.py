from ORM.wsgi import *# importamos lo modulos de la carpeta wsgi.py

from core.erp.models import Type

# Listar

#*********** HACER UNA CONSULTA ***********
query = Type.objects.all()
print(query) # muestra lo registro de la tabla Type

#********* HACER UNA INSERIONN ***********
t = Type()
#t = Type(name = "Test 1")
t.name = "Test 1"
t.save()
