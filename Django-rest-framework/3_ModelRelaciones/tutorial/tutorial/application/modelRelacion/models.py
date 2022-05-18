from tabnanny import verbose
from django.db import models

# Create your models here.

#Documentation  Model Meta Options
#https://docs.djangoproject.com/en/4.0/ref/models/options/

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=200)
    
class Ox(models.Model):
    horn_length = models.IntegerField()
    
    """class meta:
        ordering = ['horn_length']
        verbose_name_plural = "Brian"""