from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/<id>', views.blog, name="blog"),
]
