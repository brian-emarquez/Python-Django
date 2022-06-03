"""api2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Redooc Dumentacion Emcabesado
# Schema to describe documentation
# https://www.geeksforgeeks.org/how-to-automatically-create-api-documentation-in-django-rest-framework/

schema_view = get_schema_view(
    openapi.Info(
        title="Wallet 2",
        default_version='v2',
        description="It is a wallet 2 API - Brian",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="9780desarrollador07@gmail.com"),
        license=openapi.License(name="9780 Bitcoin"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('applications.authentication.urls')),
]
