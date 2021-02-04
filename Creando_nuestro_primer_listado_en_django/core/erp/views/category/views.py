from django.shortcuts import render

def category_list(request):
    data = {
        'title':'Listado de Categorias',
        'categorias': Category.objects.all()
    }
    return render(request, 'category/list.html', data)