from django.shortcuts import render, redirect
from django.views.generic import ListView

from core.erp.models import Category


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

    # dispatch
    def dispatch (self, request, *args, **kwargs):
        if request.method == 'GET':
            return redirect('erp:category_list2')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context
