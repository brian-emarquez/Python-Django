from django.urls import path
from perfiles_api import views

urlpatterns = [
    path('hello_view/', views.HelloapiView.as_view()),
]