from config.wsgi import *
from core.erp.models import *

# LISTAR

print(Category.objects.all())

for i in Category.objects.filter():
    print(i)