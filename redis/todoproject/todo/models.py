# Create your models here.
from django.db import models

# Create your models here.
class todo(models.Model):
    work = models.CharField(max_length=100)
    done = models.BooleanField(default=False)