from django.contrib import admin
from django.db.models.base import Model
from perfiles_api import models
# Register your models here.
# se registro un modelo
admin.site.register(models.UserProfile)

