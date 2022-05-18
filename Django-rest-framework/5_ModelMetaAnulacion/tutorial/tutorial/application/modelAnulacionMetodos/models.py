from django.db import models

# Create your models here.

# https://docs.djangoproject.com/en/4.0/topics/db/models/#overriding-predefined-model-methods

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        if self.name == "brian":
            return 
        else:
            super().save(*args, **kwargs)  # Call the "real" save() method.