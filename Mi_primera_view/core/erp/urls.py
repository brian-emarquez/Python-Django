from django.contrib import admin
from django.urls import path

from core.erp.views import myfirtsView

urlpatterns = [
    path('uno/', myfirtsView),
    path('dos/', myfirtsView)

]
