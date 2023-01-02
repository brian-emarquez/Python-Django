from django.db import models

# Create your models here.

class Fruits(models.Model):
    fruit_name = models.CharField(max_length=100)
    