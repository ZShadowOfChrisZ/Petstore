from django.shortcuts import render, redirect
from apps.master.models import Usuario, Producto, Categoria, Contacto
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
    collares = Producto.objects.filter(categoriaProducto = 1)
    bandanas = Producto.objects.filter(categoriaProducto = 2)
    correas = Producto.objects.filter(categoriaProducto = 3)
    context = {
        'collares' : collares,
        'correas' : correas,
        'bandanas' : bandanas,
        'titulo' : 'Tienda'
    }
    return render(request, 'tienda.html', context)

def organizaciones(request):
    context = {
        'titulo' : 'Organizaciones'
    }
    return render(request,'organizaciones.html', context)

def contacto(request):
    if request.method == 'POST':
        contacto = Contacto(
            nombre = request.POST.get('nombre'),
            apellido = request.POST.get('apellido'),
            email = request.POST.get('email'),
            telefono = request.POST.get('telefono'),
            comuna = request.POST.get('comuna')
        )
        contacto.save()
        return redirect('contacto')
    context = {
        'titulo' : 'Contacto'
    }
    return render(request, 'contacto.html', context)

def admin(request):
    if request.method == 'POST':
        usuario = Usuario.objects.filter(nombre = request.POST.get('nombre'), password = request.POST.get('password'), perfil = 1)
        if len(usuario) != 0:
            return redirect('productos')
    context = {
        'titulo' : 'Administrador'
    }
    return render(request, 'admin.html', context)

def mantenedores(request):
    context = {
        'titulo' : 'Administrar'
    }
    return render(request, 'mantenedores.html', context)

def productos(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    if request.method == 'POST':
        categoria = Categoria.objects.get(id = request.POST.get('categoriaProducto'))
        producto = Producto(
            nombreProducto = request.POST.get('nombreProducto'),
            categoriaProducto = categoria,
            precioProducto = request.POST.get('precioProducto'),
            imagenProducto = request.FILES.get('imagenProducto')
        )
        producto.save()
        return redirect('productos')
    context = {
        'categorias' : categorias,
        'productos' : productos,
        'titulo' : 'Productos'
    }
    return render(request, 'productos.html', context)

def eliminarProducto(request, idProducto):
    if request.method == "POST":
        producto = Producto.objects.get(id = idProducto).delete()
        return redirect('productos')

def contactos(request):
    contactos = Contacto.objects.all()
    context = {
        'contactos' : contactos,
        'titulo' : 'Contactos'
    }
    return render(request, 'contactos.html', context)    