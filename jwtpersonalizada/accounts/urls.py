# project.urls
# accounts.urls


from django.urls import path
from .views import login_view, profile 


urlpatterns = [
    path('profile', profile, name='profile'),
    path('login/', login_view, name='login'),
]