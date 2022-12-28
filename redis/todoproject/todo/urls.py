
from django.urls import path
from .views import TodoViewSet

urlpatterns = [
    path(
        "todo",
        TodoViewSet.as_view(
            {
                "get": "get",
                "post": "add",
            }
        ),
    ),
    path("todoAllCache/<str:key>", TodoViewSet.as_view({"get": "getCache"})),
    path("getKey/<str:key>", TodoViewSet.as_view({"get": "getKey"})),
    path("todo/<str:pk>", TodoViewSet.as_view({"put": "update", "delete": "remove"})),
]