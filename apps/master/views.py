from django.shortcuts import render

# Create your views here.

def inicio(request):
    context = {
        'titulo' : 'Inicio'
    }
    return render(request, 'index.html', context)

def nosotros(request):
    context = {
        'titulo' : 'Nosotros'
    }
    return render(request, 'nosotros.html', context)

def tienda(request):
    context = {
        'titulo' : 'Tienda'
    }
    return render(request, 'tienda.html', context)

def organizaciones(request):
    context = {
        'titulo' : 'Organizaciones'
    }
    return render(request,'organizaciones.html', context)

def contacto(request):
    context = {
        'titulo' : 'Contacto'
    }
    return render(request, 'contacto.html', context)

def admin(request):
    return render(request, 'admin.html')