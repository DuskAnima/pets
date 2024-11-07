from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="Index"),
    path("nueva", views.index, name="nueva"),
    path("lista", views.index, name="lista"),
    path("editar", views.index, name="editar"),
    path("eliminar", views.index, name="eliminar"),
]