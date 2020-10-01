from django.urls import path

from projectoWebApp import views

urlpatterns = [

    path('', views.home, name="Home"),
    path('servivios', views.servivios, name="Servivios"),
    path('tienda', views.tienda, name="Tienda"),
    path('blog', views.blog, name="Blog"),
    path('contacto', views.contacto, name="Contacto"),

]
