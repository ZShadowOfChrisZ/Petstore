from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('tienda', views.tienda, name="tienda"),
    path('organizaciones', views.organizaciones, name="organizaciones"),
    path('contacto', views.contacto, name="contacto"),
    path('administrar', views.admin, name="admin"),
]
