from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('tienda', views.tienda, name="tienda"),
    path('organizaciones', views.organizaciones, name="organizaciones"),
    path('contacto', views.contacto, name="contacto"),
    path('inicioadmin', views.admin, name="admin"),
    path('administrar', views.mantenedores, name="mantenedores"),
    path('administrar/productos', views.productos, name="productos"),
    path('administrar/eliminarProductos/<int:idProducto>', views.eliminarProducto, name="eliminarProducto"),
    path('administrar/contactos', views.contactos, name="contactos")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
