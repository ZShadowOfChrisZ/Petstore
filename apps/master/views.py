from django.shortcuts import render

# Create your views here.

def inicio(request):
    context = {
        'titulo' : 'Inicio'
    }
    return render(request, 'index.html', context)