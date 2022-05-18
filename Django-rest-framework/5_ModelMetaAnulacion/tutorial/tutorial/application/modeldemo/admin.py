from django.contrib import admin

from application.modeldemo.models import Musician, Album, Person, Runner, Student

# Register your models here.
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Person)
admin.site.register(Runner)
admin.site.register(Student)