from django.shortcuts import render

def category_list(request):
    data = {
        'title':'Listado de Categorias',
        'categorias': category.objects.all()
    }
    return render(request, 'category/list.html', data)