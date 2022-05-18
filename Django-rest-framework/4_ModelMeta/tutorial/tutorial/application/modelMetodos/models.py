from django.db import models

# Create your models here.

# https://docs.djangoproject.com/en/4.0/topics/db/models/#model-methods-1

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status_test(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            print("are you baby")
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            print("are you OLD PAPU")
            return "Post-boomer"

    # decorador
    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
    
    
    ######################### TEST SHELL #############################
    
    # from application.modelMetodos.models import Person
    # from django.contrib import admin
    # my_person = Person.objects.first()
    # my_person.baby_boomer_status_test()
    # print(my_person.baby_boomer_status_test())