import os
import sys
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


#MARIADB = {
#    'default': {
#       'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'db',
#        'USER': 'briandb',
#        'PASSWORD': 'briandb',
#        'HOST': '127.0.0.1',
#        'PORT': 3307,
#    }
#}


POSTGRES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'briandb',
        'PASSWORD': 'briandb',
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '5432',
    }
}


