## Django REST Framework (Ubuntu Linux)

<table align="center">
  <tr>
    <td align="center" style="padding=0;width=50%;">
      <img align="center" style="padding=0;" src="././images/rest.png" />
    </td>
  </tr>
</table>

## Comands

*Use Freeze*

```diff
pip freeze > requirements.txt
```

*Use django*

```diff
pip install django
```

*Use djangorestframework*

```diff
pip install djangorestframework
```

*Use pygments*

```diff
pip install pygments
```

*Install PostgreSQL Linux*

```diff
sudo apt install postgresql postgresql-contrib
```

*Sheel Django*

```diff
python manage.py shell
```


---

* Model

_Ejemplo practico_

```python
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
```

```diff
from application.modeldemo.models import *
from django.db import models
p = Person(name="Fred Flintstone", shirt_size="L")
p.save()
p.get_shirt_size_display()
```

[Model Django](https://docs.djangoproject.com/en/4.0/topics/db/models/)



_Argumentos_

<ol class="toc"><li><a href="#argumento-cascade">Argumento <code>CASCADE</code></a></li><li><a href="#argumento-protect">Argumento <code>PROTECT</code></a></li><li><a href="#argumento-restrict">Argumento <code>RESTRICT</code></a></li><li><a href="#argumento-set_null">Argumento <code>SET_NULL</code></a></li><li><a href="#argumento-set_default">Argumento <code>SET_DEFAULT</code></a></li><li><a href="#set-argumento"><code>SET()</code> Argumento</a></li><li><a href="#argumento-do_nothing">Argumento <code>DO_NOTHING</code></a></li></ol>

[Función del parámetro - Argumentos](https://www.delftstack.com/es/howto/django/django-on_delete-parameter/)


_Relaciones_

[Many-to-one relationships](https://docs.djangoproject.com/en/4.0/topics/db/models/#relationships)

```python
from django.db import models

class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)
```

[Many-to-one relationships](https://docs.djangoproject.com/en/4.0/topics/db/models/#many-to-many-relationships)

[One-to-one relationships](https://docs.djangoproject.com/en/4.0/topics/db/models/#one-to-one-relationships)


* Serializers

Documentation [Serializers](https://www.django-rest-framework.org/tutorial/quickstart/#serializers)

Notice that we're using hyperlinked relations in this case with HyperlinkedModelSerializer. You can also use primary key and various other relationships, but hyperlinking is good RESTful design.

---

## WSL 

```diff	
wsl --install -d ubuntu
```

[Instalación de WSL](https://docs.microsoft.com/es-es/windows/wsl/install#install)


## PostgreSQL


```diff	
sudo apt install postgresql postgresql-contrib
```

_Tutorial PostgraSQL_

Comience a usar la herramienta de línea de comandos de PostgreSQL - [PostgreSQL](https://www.cherryservers.com/blog/how-to-install-and-setup-postgresql-server-on-ubuntu-20-04)

