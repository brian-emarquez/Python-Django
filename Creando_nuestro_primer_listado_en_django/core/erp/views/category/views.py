from django.shortcuts import render

def category_list(request):
    data = {

    }
    return render(request, 'category/list.html', data)