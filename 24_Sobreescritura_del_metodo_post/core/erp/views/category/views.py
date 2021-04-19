from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from core.erp.models import Category
from django.contrib.auth.decorators import login_required



def category_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)

# Vista basadas en clases, usando herencia
class CategoryListView(ListView): #Herencia
    model = Category
    template_name = 'category/list.html'

    # dispatch Y decorador
    @method_decorator(login_required) # Validador de usuarios
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context
