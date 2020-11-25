from panel_administrador.wsgi import * # importamos lo modulos de la carpeta wsgi.py
from core.erp.model import *

# LISTAR

for i in Category.objects.filter():
    print(i)