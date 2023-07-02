from django.shortcuts import render

# Create your views here.

def inicio(request):
    context = {
        'titulo' : 'Inicio'
    }
    return render(request, 'index.html', context)

def tienda(request):
    context = {
        'titulo' : 'Tienda'
    }
    return render(request, 'tienda.html', context)

def admin(request):
    return render(request, 'admin.html')