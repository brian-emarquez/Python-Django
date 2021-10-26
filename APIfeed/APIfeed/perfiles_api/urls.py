from django.urls import path, include
from rest_framework import routers

from rest_framework.routers import DefaultRouter
# VIEWS
from perfiles_api import views

router = DefaultRouter()
router.register('hello_viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewsSet)

urlpatterns = [
    path('hello_view/', views.HelloapiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]