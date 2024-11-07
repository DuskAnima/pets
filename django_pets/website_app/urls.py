from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("blog", views.index, name="blog"),
    path("nosotros", views.index, name="nosotros"),
    path("contacto", views.index, name="contacto"),
    path("productos", views.index, name="productos")
]