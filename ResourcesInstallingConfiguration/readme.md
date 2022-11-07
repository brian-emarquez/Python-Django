## Resources for installing Configuration

## JET (django-jet 4) & REDOC

```
pip install https://github.com/Barukimang/django-jet/archive/dev.zip
```

Se presenta la manera de insltalar Jet 4 en Django.

[Mojtaba-saf/django-jet](https://github.com/Mojtaba-saf/django-jet)

```
pip install https://github.com/Barukimang/django-jet/archive/dev.zip
# or
easy_install https://github.com/Barukimang/django-jet/archive/dev.zip


_Ejemple_


* Setting.py

```python
INSTALLED_APPS = [
    # -----------: jet :---------------
    'jet',
    'jet.dashboard',
    'django.contrib.admin',
    
    # -----------: Redoc :---------------
    'coreapi', 
    'drf_yasg',.
    ...
]
```

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]
```
```python

JET_SIDE_MENU_COMPACT = True
JET_THEMES = [
    {
        'theme': 'default', # theme folder name
        'color': '#47bac1', # color of the theme's button in user menu
        'title': 'Default' # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]
```


* urls.py

```python
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
```

```python
schema_view = get_schema_view(
    openapi.Info(
        title="example",
        default_version='v1',
        description="It is a example API created to" + 
        " get, post, update data related to project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="email.com@gmail.com"),
        license=openapi.License(name="example_enterprice"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
```

```python
schema_view = get_schema_view(
    openapi.Info(
        title="example",
        default_version='v1',
        description="It is a example API created to" + 
        " get, post, update data related to project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="email.com@gmail.com"),
        license=openapi.License(name="example_enterprice"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
```


## GRAPH MODELS

* Setting.py 

```python
GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
    'app_labels': ['app1', 'app2'...],
}
```

```python
pip install django-extensions
pip install pydotplus
```

```python
INSTALLED_APPS = (
    ...
    'django_extensions',
    ...
)
```

* Run command:

```python
python manage.py graph_models -a -o p2phelper.png
```

I also had this problem on Ubuntu 16.04.

Fixed by running `sudo apt-get install graphviz` in addition to the pip install I had already performed.
