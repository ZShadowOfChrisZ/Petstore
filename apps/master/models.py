from django.db import models

class PerfilUsuario(models.Model):
    nombrePerfil = models.CharField(max_length=50)

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    perfil = models.ForeignKey("PerfilUsuario", on_delete=models.CASCADE)
    password = models.CharField(max_length=50)

class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=50)

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=50)
    categoriaProducto = models.ForeignKey("Categoria", on_delete=models.CASCADE)
    precioProducto = models.IntegerField()
    imagenProducto = models.ImageField(upload_to="productos", max_length=200)

class Venta(models.Model):
    cliente = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    productos = models.ManyToManyField("Producto")
    fechaVenta = models.DateTimeField(auto_now_add=True)

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    telefono = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)