from django.urls import path,include, reverse_lazy
from .views import (
    MyTokenObtainPairView,
    
)


urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token'),
    
]
    