from .models import todo
from .serializers import TodoSerializer


def get():
    Todo = todo.objects.all()
    serializer = TodoSerializer(Todo, many=True)
    return serializer.data


def add(request):
    serializer = TodoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def update(request, pk=None):
    updateTodo = todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=updateTodo, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def remove(request, pk=None):
    Todo = todo.objects.get(id=pk)
    Todo.delete()
    return "deleted"