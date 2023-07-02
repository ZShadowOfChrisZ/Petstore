from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('tienda', views.tienda, name="tienda"),
    path('administrar', views.admin, name="admin"),
    path('contacto', views.contacto, name="contacto")
]
