## ViewSets

Usamos funciones de opeadores de modelo <br>

```python
def list()
def create()
def update()
def partial_update()
def destroy()
```
*Que son los ViewSets*

- se encargan de la logica comun
- bueno para operaciones estandar
- Forma mas rapida de hacer interdas con bd

*Cuando Usamos Viewsets*

- CRUD Simple
- API Simple
- Poca personalizacion de logica
- Trabaja con estructuras de datos normales

_Requerimientos_

```python
from rest_framework import viewsets
```

