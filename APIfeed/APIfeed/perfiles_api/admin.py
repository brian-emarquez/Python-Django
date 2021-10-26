from django.contrib import admin
from django.db.models.base import Model
from perfiles_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)

