
<h2 align="center">🦄Framework Web -- Learn Django</h2>

<p align="center">
    
  <a href="https://github.com/BrianMarquez3/Python-Django/tags">
    <img src="https://img.shields.io/github/tag/BrianMarquez3/Python-Django.svg?label=version&style=flat" alt="Version">
  </a>
  <a href="https://github.com/BrianMarquez3/Python-Django/stargazers">
    <img src="https://img.shields.io/github/stars/BrianMarquez3/Python-Django.svg?style=flat" alt="Stars">
  </a>
  <a href="https://github.com/BrianMarquez3/Python-Django/network">
    <img src="https://img.shields.io/github/forks/BrianMarquez3/PPython-Django.svg?style=flat" alt="Forks">
  </a>
   </a>  
 </a>
   <a href="https://github.com/BrianMarquez3/Python-Django/network">
    <img src="https://img.shields.io/badge/Plataform-Windows-blue">
  </a>
 </p>

![django](./Images/django.png)

## Tabla de Contenidos

| Numeration       | Check         |Topic                   |
| ---------------- |---------------|----------------------- |
| 1                |✔️            | [Que es Django ](#Que-es-Django) | 
| 2                |✔️            | [Instalador ](#Instalador) |
| 3                |✔️            | [Modelo Vista Controlador  ](#Modelo-Vista-Controlador) | 
| 4                |✔️            | [Características ](#Características) | 
| 5                |✔️            | [Principales Comandos ](#Principales-Comandos) |
| 6                |✔️            | [Base de datos](#Base-de-datos) |
| 7                |✔️            | [Manejo de datos por Consola ](#Manejo-de-datos-por-Consola) |
| 8                |✔️            | [Arquitectura](#Arquitectura) |
| 9                |✔️            | [Jerarquia u orden de llamadas desde plantilla](#Jerarquia-u-orden-de-llamadas-desde-plantilla) |
| 10                |✔️            | [API Forms ](#api-form) |
| 11                |✔️            | [Proyecto vs Aplicacion ](#Proyecto-vs-Aplicacion) |
| 12                |✔️            | [Pycharm ](#Pycharm) |
| 13                |✔️            | [Envio de Email ](#Envio-de-Email) |
| 15                |✔️            | [Models ](#Models ) |
| 16                |✔️            | [ORM ](#ORM ) |
| 17                |✔️            | [Archivos estaticos](#Archivos-estaticos) |
| 18                |✔️            | [Views](#views) |
| 19                |✔️            | [Parametros](#Parametros) |
| 20                |✔️            | [Plantillas](#plantillas) |
| 21                |✔️            | [Panel de Administrador](#Panel-de-Administrador) |
| 22                |✔️            | [ListView vistas basadas en clases](#ListView-vistas-basadas-en-clases) |
| 22                |✔️            | [ListView II vistas basadas en clases](#ListView-II-vistas-basadas-en-clases) |
| 23                |✔️            | [Sobreescritura del metodo dispatch](#Sobreescritura-del-metodo-dispatch) |
| 24                |✔️            | [Implementando decoradores](#Implementando-decoradores) |

---

## Que es Django 

Django es un framework de desarrollo web de código abierto, escrito en Python, que respeta el patrón de diseño conocido como MVC (Modelo–Vista–Controlador). Fue desarrollado en origen para gestionar varias páginas orientadas a noticias de la World Company de Lawrence, Kansas, y fue liberada al público bajo una licencia BSD en julio de 2005; el framework fue nombrado en alusión al guitarrista de jazz gitano Django Reinhardt. En junio de 2008 fue anunciado que la recién formada Django Software Foundation se haría cargo de Django en el futuro.

La meta fundamental de Django es facilitar la creación de sitios web complejos. Django pone énfasis en el re-uso, la conectividad y extensibilidad de componentes, el desarrollo rápido y el principio No te repitas (DRY, del inglés Don't Repeat Yourself). Python es usado en todas las partes del framework, incluso en configuraciones, archivos, y en los modelos de datos. [WIKIPEDIA](https://es.wikipedia.org/wiki/Django_(framework)#:~:text=Django%20es%20un%20framework%20de,vista%E2%80%93controlador%20(MVC).&text=En%20junio%20de%202008%20fue,de%20Django%20en%20el%20futuro.) <br>

### Framework

Un Framework es un marco de trabajo formado por un conjunto de herramientas, librerias y buenas practicas.

### Para qué Sirve Django

- Para crear sitios web (Complejos) de forma rapida y sencilla
- Hay tareas que son repetitivas, pesadas y comunes en el momento de crear deferentes sitios web, django viene a facilitar la realizacion de estas tareas.
- Hay codigos que podemos reutilizar de un sitio web a otro, Django tambien nos permite esta reutilizacion de forma sencilla.

---

## Instalador

📦 [Install Django](https://www.djangoproject.com/) Intalador de Django.<br>
📦 [Install PyCham](https://www.jetbrains.com/es-es/pycharm/download/#section=windows) Intalador de PyCham.<br>
📦 [Install Python](https://www.python.org/) Instalador de Python.<br>

---
##  Modelo Vista Controlador 

- Model Template View
![django](./Images/MTV1.jpg)

---
## Características

- Un mapeador objeto-relacional.
- Aplicaciones "enchufables" que pueden instalarse en cualquier página gestionada con Django.
- Una API de base de datos robusta.
- Un sistema incorporado de "vistas genéricas" que ahorra tener que escribir la lógica de ciertas tareas comunes.
- Un sistema extensible de plantillas basado en etiquetas, con herencia de plantillas.
- Un despachador de URLs basado en expresiones regulares.
- Soporte de internacionalización, incluyendo traducciones incorporadas de la interfaz de administración.

---

## Principales Comandos

_Install Django_

[www.djangoproject.com](https://www.djangoproject.com/download/)
```
pip install Django==X.X.X
```
_Actualiza Django_
```
pip install --upgrade Django
```
_Version de Django_

```
import django | django.VERSION
```

_Primer Projecto_

```
django-admin startproject nombreProyecto
```

_Ejecutar Servidor Django_

```
python manage.py runserver
```
_Crear Aplicacion_

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
python manage.py sqlmigrate nombreAplicacion 000n
```
_Migrate_

```
python manage.py migrate
```

_Shell_

```
python manage.py shell
```

_mysqlclient_

```
pip install mysqlclient
```

_Django- yodbc azure_

```
pip install django-pyodbc-azure
```

---
## Base de datos

_Principales conectores a gestores de base de datos_
### Crear Super Usuario

```
python manage.py createsuperuser
```

### Conector PostgreSQL

_Driver_
```
pip install psycopg2
```

_Libreria_
```
pip install mysqlclient
```
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'articulosclientes',
        'USER': 'briandb',
        'PASSWORD': 'briandb',
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '5432',
}
```

### Conector Mysql/MariaDb 

```
pip3 install mariadb
```

```
pip install mysqlclient
```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'articulosclientes',
        'USER': 'briandb',
        'PASSWORD': 'briandb',
        'HOST': '127.0.0.1',
        'PORT': 3307,
    }
}
```
### Conector SQLSERVER

_Driver_
```
https://www.microsoft.com/es-es/download/details.aspx?id=56567

```
_Libreria_

```
pip install pyodbc
```

_Conectar Python Django con SQL Server_

```python
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'db_almacen',
        'USER': 'usr_almacen',
        'PASSWORD': 'mipassword',
        'HOST': '127.0.0.1',
        'PORT': '1433',

        'OPTIONS': {
            'driver': 'ODBC Driver 13 for SQL Server',
        },
    }
}
```
### Django BBDD

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

| Carpeta                    | Link |     
|----------------------------|:-----------:|
| [BAse de Datos Config](Data_Base_Config)          |      ✔️     | 

---
## Manejo de datos por Consola
### Insertar datos BBDD - Consola

```python
from nombreAplicacion.models import nombreTabla
art=nombreTabla(inten1='nombre', iten2='nombre', iten3=numero)
art.save()
#art2= nombreTabla.objects.create(iten1="nombre", iten2="campo", iten3=numero)   
```
### Actualizar datos BBDD - Consola

```python
from nombreAplicacion.models import nombreTabla
art.precio=100 
art.save
```

### Borrar datos BBDD - Consola

```python
from nombreAplicacion.models import nombreTabla
variableborrar=nombeTabla.objects.get(id=3) 
variableborrar.delete()
```
---

## Arquitectura

Aunque Django está fuertemente inspirado en la filosofía de desarrollo Modelo Vista Controlador, sus desarrolladores declaran públicamente que no se sienten especialmente atados a observar estrictamente ningún paradigma particular, y en cambio prefieren hacer "lo que les parece correcto". Como resultado, por ejemplo, lo que se llamaría "controlador" en un "verdadero" framework MVC se llama en Django "vista", y lo que se llamaría "vista" se llama "plantilla". [WIKIPEDIA](https://es.wikipedia.org/wiki/Django_(framework)).<br>

- Presentacion
- Control
- Mediator
- Entity
- Foundation

---
## Jerarquia u orden de llamadas desde plantilla

-   Diccionario
-   Atributo
-   Metodo
-   Indice de lista

---


## API FORM

```
from nombreAplicacion.forms import FormularioContacto 
miformulario = FormularioContacto()
```
_Mostrar Formulario_
print(miformulario)

| Carpeta                    | Link |     
|----------------------------|:-----------:|
| [API FORM](https://github.com/BrianMarquez3/Python-Django/tree/master/API_Forms)          |      ✔️     | 

---

## Proyecto vs Aplicacion

![django](./Images/proyectoApliacion.png)

## Pycharm

_Pagina Principal_ [ JETBRAINS](https://www.jetbrains.com/es-es/pycharm/).<br>

![django](./Images/pycharm.png)

### Configuración Entorno Pycharm

_Pantalla de creacion de Proyecto_

![django](./Images/conf.png)

- Carpeta
    -   app : Aqui se coloca todos lo archivos
    -   env : Aqui Se coloca la version Python

---
## Envio de Email
_Incresar en el Archivo Setting_

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST="smtp.gmail.com"
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER="tuemail@gmail.com"
EMAIL_HOST_PASSWORD="tupassword"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
```

- Ingresar al Shell para las Pruebas
```
from django.core.mail import send_mail   
```
```
send_mail('el asusntoo', 'mensaje del correo, 'tu correo', ['correo destinatario'], fail_silently=False,)
```

| Carpeta                    | Link |     
|----------------------------|:-----------:|
| [Envio de Email](https://github.com/BrianMarquez3/Python-Django/tree/master/TiendaOnline_EnvioEmails)          |      ✔️     | 

---
## Models 

Un modelo es la fuente única y definitiva de información sobre sus datos. Contiene los campos y comportamientos esenciales de los datos que está almacenando. Generalmente, cada modelo se asigna a una sola tabla de base de datos.
[DOCS.DJANGOPROJECT](https://docs.djangoproject.com/en/3.1/topics/db/models/).<br>

![django](./Images/models.png)

| Carpeta                    | Link |     
|----------------------------|:-----------:|
| [Model](https://github.com/BrianMarquez3/Python-Django/tree/master/Models)          |      ✔️     | 
| [Model Relaciones](https://github.com/BrianMarquez3/Python-Django/tree/master/Models_II_Relaciones)          |      ✔️     | 


---

## ORM

Un ORM es un modelo de programación que permite mapear las estructuras de una base de datos relacional (SQL Server, Oracle, MySQL, etc.), en adelante RDBMS (Relational Database Management System), sobre una estructura lógica de entidades con el objeto de simplificar y acelerar el desarrollo de nuestras aplicaciones.

| Carpeta                    | Link |     
|----------------------------|:-----------:|
| [ORM I](https://github.com/BrianMarquez3/Python-Django/tree/master/ORM)          |      ✔️     | 
| [ORM II](https://github.com/BrianMarquez3/Python-Django/tree/master/ORM_II)          |      ✔️     | 

---

## Archivos estaticos

- Archivos Estaticos
  
[Documentacion Django](https://docs.djangoproject.com/en/3.1/howto/static-files/) Archivos Estaticos.<br>
  
- Bootstrap

[Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/download/) Descargar Bootstrap.<br>

- Ejemplo

[w3schools](https://www.w3schools.com/bootstrap4/bootstrap_get_started.asp) Ejemplo.<br>

| Carpeta                    | Link |     
|----------------------------|:-----------:|
| [Archivos_estaticos](https://github.com/BrianMarquez3/Python-Django/tree/master/Archivos_estaticos)          |      ✔️     | 


---
## Views

* VIEW
_Modelo Vista controlador_
```
M = Modelo (Base de Datos)
V = Vista
C = Controlador (Funciones)
```

_Modelo Vista Template_

```
M = Modelo (Base de Datos)
V = Vista (Funciones)
C = Templates (Pantallas)
```

| Carpeta                    | Link |     
|----------------------------|:-----------:|
| [Mi Primera View](https://github.com/BrianMarquez3/Python-Django/tree/master/Mi_primera_view)          |      ✔️     | 

---
## Parametros

| Carpeta                    | Link |     
|----------------------------|:-----------:|
| [Paramentros URL](https://github.com/BrianMarquez3/Python-Django/tree/master/ParametroURL)          |      ✔️     | 
| [Parametros En URL](https://github.com/BrianMarquez3/Python-Django/tree/master/ParametrosEnURL)          |      ✔️     | 

---
## Plantillas

| Carpeta                    | Link |     
|----------------------------|:-----------:|
| [PLantillas I](https://github.com/BrianMarquez3/Python-Django/tree/master/Plantillas)          |      ✔️     | 
| [PLantillas II](https://github.com/BrianMarquez3/Python-Django/tree/master/PlantillasII)          |      ✔️     | 
| [PLantillas III](https://github.com/BrianMarquez3/Python-Django/tree/master/PlantillasIII)          |      ✔️     | 
| [PLantillas IV](https://github.com/BrianMarquez3/Python-Django/tree/master/PlantillasIV)          |      ✔️     | 
| [PLantillas V ](https://github.com/BrianMarquez3/Python-Django/tree/master/PlantillasV)          |      ✔️     | 
| [PLantillas IV](https://github.com/BrianMarquez3/Python-Django/tree/master/PlantillasVI)          |      ✔️     | 
| [Templates I](https://github.com/BrianMarquez3/Python-Django/tree/master/Templates_I)          |      ✔️     | 
| [Templates II](https://github.com/BrianMarquez3/Python-Django/tree/master/Templates_II)          |      ✔️     | 
| [Templates Integrando Platntilla adminLT3](https://github.com/BrianMarquez3/Python-Django/tree/master/Templates_III_%20Integrando_Platntilla_adminLT3)          |      ✔️     | 

---

## Panel de Administrador

| Carpeta                    | Link |     
|----------------------------|:-----------:|
| [Panel de Adminitracion](https://github.com/BrianMarquez3/Python-Django/tree/master/panel_administrador)          |      ✔️     | 


## ListView vistas basadas en clases


| Carpeta                    | Link |     
|----------------------------|:-----------:|
| [ListView_vistas_basadas_en_clases](https://github.com/BrianMarquez3/Python-Django/tree/master/ListView_vistas_basadas_en_clases)          |      ✔️     | 

---

## ListView II vistas basadas en clases


| Carpeta                    | Link |     
|----------------------------|:-----------:|
| [ListView II_vistas_basadas_en_clases](https://github.com/BrianMarquez3/Python-Django/tree/master/ListView_II_Vistas_basadas_en_clases)          |      ✔️     | 

---

## Sobreescritura del metodo dispatch 

| Carpeta                    | Link |     
|----------------------------|:-----------:|
| [Sobreescritura del metodo dispatch](https://github.com/BrianMarquez3/Python-Django/tree/master/Sobreescritura_del_metodo_dispatch)          |      ✔️     |

---

## Implementando decoradores

_Documentacion_

[Decoradores Django](https://pywombat.com/articles/decoradores-django)

| Carpeta                    | Link |     
|----------------------------|:-----------:|
| [Implementando decoradores](https://github.com/BrianMarquez3/Python-Django/tree/master/Implementando_decoradores)          |      ✔️     |

---
## 
## Spotify Django
Music Python [List on Spotify](https://open.spotify.com/playlist/11AwbhmXyh2jKlsHmaxcP9)

![python](./Images/django2.jpg)

---

## Paypal

🩸 Hacer una donación [PAYPAL](https://www.paypal.com/donate?hosted_button_id=98U3T62494H9Y) 🍵



