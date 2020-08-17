
<h2 align="center">Learn Django &nbsp;:heart:&nbsp;</h2>

![django](./Images/django.png)

## ¿Que es Django? 💻

Django es un framework de desarrollo web de código abierto, escrito en Python, que respeta el patrón de diseño conocido como MVC (Modelo–Vista–Controlador). Fue desarrollado en origen para gestionar varias páginas orientadas a noticias de la World Company de Lawrence, Kansas, y fue liberada al público bajo una licencia BSD en julio de 2005; el framework fue nombrado en alusión al guitarrista de jazz gitano Django Reinhardt. En junio de 2008 fue anunciado que la recién formada Django Software Foundation se haría cargo de Django en el futuro.

La meta fundamental de Django es facilitar la creación de sitios web complejos. Django pone énfasis en el re-uso, la conectividad y extensibilidad de componentes, el desarrollo rápido y el principio No te repitas (DRY, del inglés Don't Repeat Yourself). Python es usado en todas las partes del framework, incluso en configuraciones, archivos, y en los modelos de datos.

## Framework

Un Framework es un marco de trabajo formado por un conjunto de herramientas, librerias y buenas practicas.

## ¿Para qué Sirve Django?

- Para crear sitios web (Complejos) de forma rapida y sencilla
- Hay tareas que son repetitivas, pesadas y comunes en el momento de crear deferentes sitios web, django viene a facilitar la realizacion de estas tareas.
- Hay codigos que podemos reutilizar de un sitio web a otro, Django tambien nos permite esta reutilizacion de forma sencilla.

##  Modelo Vista Controlador (Model Template View)
![django](./Images/MTV.png)

## Características

- Un mapeador objeto-relacional.
- Aplicaciones "enchufables" que pueden instalarse en cualquier página gestionada con Django.
- Una API de base de datos robusta.
- Un sistema incorporado de "vistas genéricas" que ahorra tener que escribir la lógica de ciertas tareas comunes.
- Un sistema extensible de plantillas basado en etiquetas, con herencia de plantillas.
- Un despachador de URLs basado en expresiones regulares.
- Soporte de internacionalización, incluyendo traducciones incorporadas de la interfaz de administración.

## Comandos

_Install Django - 3.0.8_

```
pip install Django==3.0.8
```
_Version de Django_

```
import django | django.VERSION
```

_Primer Proyecto_

```
django-admin startproject PrimerProyecto
```

_Ejecutar Servidor Django_

```
python manage.py runserver
```
_Crear Aplicacion - consola_

```
python manage.py startapp nombreAplicacion
```

_Check de la Aplicacion_

```
python manage.py check nombreAplicacion
```

_Generar la Base de Datos_

```
python manage.py makemigrations
```

_Generar Codigo SQL_

```
python manage.py sqlmigrate nobreAplicacion 000n
```
_Migrate_

```
python manage.py migrate
```

_Shell_

```
python manage.py shell
```
## Ingreso de datos BBDD

```
from gestionPedido.models import Articulos
art=Articulos(nombre='mesa', seccion='decoracion', precio=50) 

```

## Arquitectura

Aunque Django está fuertemente inspirado en la filosofía de desarrollo Modelo Vista Controlador, sus desarrolladores declaran públicamente que no se sienten especialmente atados a observar estrictamente ningún paradigma particular, y en cambio prefieren hacer "lo que les parece correcto". Como resultado, por ejemplo, lo que se llamaría "controlador" en un "verdadero" framework MVC se llama en Django "vista", y lo que se llamaría "vista" se llama "plantilla". [WIKIPEDIA](https://es.wikipedia.org/wiki/Django_(framework)).<br>

- Presentacion
- Control
- Mediator
- Entity
- Foundation

## Jerarquia u orden de llamadas desde plantilla

-   Diccionario
-   Atributo
-   Metodo
-   Indice de lista

## Instalador

📦 [Install Django](https://www.djangoproject.com/) Intalador de Django.<br>
📦 [Install Python](https://www.python.org/) Instalador de Python.<br>

## Django BBDD

Soportados Oficialmente:
- SQLite3 : Gestor de BBDD por defecto
- PostgreSQL: Gestor Recomendado
- MySql
- Oracle

Con conectores ofrecidos por terceros:
- SQL Server
- SAP SQL
- DB2
- Firebird

## Proyecto vs Aplicacion

![django](./Images/proyectoApliacion.png)

## Spotify
Music Python [List on Spotify](https://open.spotify.com/playlist/11AwbhmXyh2jKlsHmaxcP9)

![python](./Images/django2.jpg)

